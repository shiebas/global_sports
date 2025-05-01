document.addEventListener('DOMContentLoaded', function() {
    const continentSelect = document.getElementById('id_continent');
    const bodySelect = document.getElementById('id_regional_body');

    if (!continentSelect || !bodySelect) return;

    // Get the correct endpoint URL
    function getEndpoint() {
        // Check if we're in admin
        if (window.location.pathname.includes('/admin/')) {
            return '/admin/geography/get-bodies/';
        }
        return '/api/regional-bodies/';
    }

    async function loadBodies() {
        const continentId = continentSelect.value;
        if (!continentId) {
            updateBodySelect([], 'Select continent first');
            return;
        }

        showLoadingState();

        try {
            const response = await fetch(
                `${getEndpoint()}?continent_id=${continentId}`,
                {
                    headers: {
                        'Accept': 'application/json',
                        'X-Requested-With': 'XMLHttpRequest'
                    }
                }
            );

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const bodies = await response.json();
            updateBodySelect(bodies, '---------');

        } catch (error) {
            console.error('Failed to load regional bodies:', error);
            updateBodySelect([], 'Service unavailable');
        }
    }

    function showLoadingState() {
        bodySelect.innerHTML = '<option value="">Loading...</option>';
        bodySelect.disabled = true;
    }

    function updateBodySelect(bodies, defaultText) {
        const currentValue = bodySelect.value;
        let options = `<option value="">${defaultText}</option>`;

        bodies.forEach(body => {
            const selected = body.id == currentValue ? ' selected' : '';
            const displayText = body.code ? `${body.name} (${body.code})` : body.name;
            options += `<option value="${body.id}"${selected}>${displayText}</option>`;
        });

        bodySelect.innerHTML = options;
        bodySelect.disabled = false;
    }

    // Initialize
    continentSelect.addEventListener('change', loadBodies);

    // Load immediately if value exists
    if (continentSelect.value) {
        loadBodies();
    }
});