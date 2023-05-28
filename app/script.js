$(document).ready(function() {
    // Für jeden Bereichsschieberegler
    $("input[type='range']").each(function () {
        // Anfangswert anzeigen
        var display = $($(this).data("display"));
        display.text($(this).val());

        // Bei Änderung aktualisieren
        $(this).on("input", function () {
            display.text($(this).val());
        });
    });
});