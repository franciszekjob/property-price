document.body.onload = function () {
    const citySelect = document.getElementById("citySelect");
    const locationSelect = document.getElementById("locationSelect");

    const locations = [
        // Kraków
        [
            'Bieńczyce',
            'Bieżanów - Prokocim',
            'Bronowice',
            'Dębniki',
            'Grzegórzki',
            'Krowodrza',
            'Łagiewniki - Borek Fałęcki',
            'Mistrzejowice',
            'Nowa Huta',
            'Podgórze',
            'Podgórze Duchackie',
            'Prądnik Biały',
            'Prądnik Czerwony',
            'Śródmieście',
            'Stare Miasto',
            'Swoszowice',
            'Wzgórza Krzesławickie',
            'Zwierzyniec'
        ],
        // Warszawa
        [
            'Aleksandrów',
            'Bemowo',
            'Białołęka'
        ],
        // Łódź
        [

        ],
        // Wrocław
        [

        ],
    ];

    citySelect.onchange = function () {
        locationSelect.innerHTML = ""
        locations[this.value].forEach((location, index) => {
            let option = document.createElement('option');
            option.value = index;
            option.textContent = location;
            locationSelect.appendChild(option);
        })

    }
}