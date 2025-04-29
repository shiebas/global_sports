document.addEventListener('DOMContentLoaded', function() {
    const PROD_MODE = true;
    const continentSelect = document.getElementById('id_continent');
    const bodySelect = document.getElementById('id_regional_body');

    if (!continentSelect || !bodySelect) return;

    // Production-safe URL construction
    function getEndpoint() {
        const currentPath = window.location.pathname;
        const adminBase = currentPath.split('/').slice(0, 3).join('/');
        return `${adminBase}/regionalbody/get-bodies/`;
    }

    async function loadBodies() {
        const continentId = continentSelect.value;
        if (!continentId) {
            bodySelect.innerHTML = '<option value="">Select continent first</option>';
            return;
        }

        try {
            const response = await fetch(
                `${getEndpoint()}?continent_id=${continentId}`,
                {
                    credentials: 'same-origin',
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest'
                    }
                }
            );

            if (!response.ok) throw new Error(`HTTP ${response.status}`);

            const bodies = await response.json();

            // Preserve current selection
            const currentValue = bodySelect.value;
            bodySelect.innerHTML = '';

            // Add default option
            const defaultOption = new Option('---------', '');
            bodySelect.add(defaultOption);

            // Add retrieved options
            bodies.forEach(body => {
                const option = new Option(body.name, body.id);
                bodySelect.add(option);
                if (body.id == currentValue) {
                    bodySelect.value = currentValue;
                }
            });

        } catch (error) {
            if (PROD_MODE) {
                console.error('Failed to load regional bodies');
                bodySelect.innerHTML = '<option value="">Service unavailable</option>';
            } else {
                throw error;
            }
        }
    }

    // Initialize
    continentSelect.addEventListener('change', loadBodies);
    if (continentSelect.value) loadBodies();
});