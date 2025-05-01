document.addEventListener('DOMContentLoaded', function() {
    const continentSelect = document.getElementById('id_continent');
    const bodySelect = document.getElementById('id_regional_body');

    if (!continentSelect || !bodySelect) return;

    // Get CSRF token for AJAX requests
    function getCSRFToken() {
        return document.querySelector('[name=csrfmiddlewaretoken]').value;
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
                '/admin/regionalbody/get-bodies/?continent_id=' + continentId,
                {
                    method: 'GET',
                    headers: {
                        'Accept': 'application/json',
                        'X-Requested-With': 'XMLHttpRequest',
                        'X-CSRFToken': getCSRFToken()
                    },
                    credentials: 'same-origin'
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
            options += `<option value="${body.id}"${selected}>${body.name} (${body.code})</option>`;
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