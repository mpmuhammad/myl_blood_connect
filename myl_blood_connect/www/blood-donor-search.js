
frappe.ready(function () {
    const unitFilter = document.getElementById("unit-filter");
    const bloodFilter = document.getElementById("blood-filter");
    const searchButton = document.getElementById("search-donors");
    const results = document.getElementById("donor-results");

    function escapeHTML(value) {
        return String(value ?? "").replace(/[&<>"']/g, function (char) {
            return {
                "&": "&amp;",
                "<": "&lt;",
                ">": "&gt;",
                '"': "&quot;",
                "'": "&#39;"
            }[char];
        });
    }

    function renderDonors(donors) {
        if (!donors.length) {
            results.innerHTML =
                '<div class="col-12">No matching donors found.</div>';
            return;
        }

        results.innerHTML = donors.map(function (donor) {
            return `
                <div class="col-md-4 mb-3">
                    <div class="card h-100 p-3">
                        <h5>${escapeHTML(donor.full_name)}</h5>
                        <h7>${escapeHTML(donor.house_name)}</h7>
                        <div>
                            <strong>Blood Group:</strong>
                            <span class="text-danger">
                                ${escapeHTML(donor.blood_group)}
                            </span>
                        </div>
                        <div>
                            <strong>Unit:</strong>
                            ${escapeHTML(donor.unit)}
                        </div>
                        <div>
                            <strong>Mobile Number:</strong>
                            ${escapeHTML(
                                donor.mobile_number
                            )}
                        </div>
                    </div>
                </div>
            `;
        }).join("");
    }

    searchButton.addEventListener("click", function () {
        searchButton.disabled = true;
        results.textContent = "Searching donors...";

        frappe.call({
            method: "myl_blood_connect.www.blood-donor-search.search_donors",
            args: {
                unit: unitFilter.value,
                blood_group: bloodFilter.value
            },
            callback: function (response) {
                renderDonors(response.message || []);
            },
            error: function () {
                results.textContent =
                    "Unable to load donors. Please try again.";
            },
            always: function () {
                searchButton.disabled = false;
            }
        });
    });
});
