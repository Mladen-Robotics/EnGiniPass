let cathegories_list = document.querySelector("#cathegories_wrapper");
const cathegories_input = document.querySelector("#cathegories_input_field input");
const current_cathegory = document.querySelector("#current_cathegory");
const remove_cathegory = document.querySelector("#remove_cathegory");
const cathegories_placeholder = document.querySelector("#cathegories_placeholder");
const generate = document.querySelector("#generate");
const cathegory_input_hidden = document.querySelector("#cathegory_input_hidden");
console.log(current_cathegory);

let abc = [
    {
        "title": "Sport",
        "image": "{% static 'password_dashboard/cathegories_images/sport.svg' %}",
        "tags": ["sport", "basketball", "volleybal", "tennis", "baseball", "swimming", "cricket", "exercise", "gym", "workout"]
    },
    {
        "title": "Social media",
        "image": "{% static 'password_dashboard/cathegories_images/social_media.svg' %}",
        "box-image": "cathegories_images/social_media_box.svg",
        "box-color": "#00A6FC",
        "tags": ["social", "media", "facebook", "viber", "twitter", "instagram"]
    },
    {
        "title": "Programming and IT",
        "image": "{% static 'password_dashboard/cathegories_images/programming_it.svg' %}",
        "tags": ["programming", "it", "artificial", "intelligence", "machine", "learning", "ai", "web", "frontend", "backend", "fullstack", "computer", "pc"]
    },
    {
        "title": "Cooking",
        "image": "{% static 'password_dashboard/cathegories_images/cooking.svg' %}",
        "tags": ["cooking", "kitchen", "dish", "soup", "receipt", "chef"]
    },
    {
        "title": "Art / Drawing",
        "image": "{% static 'password_dashboard/cathegories_images/art_drawing.svg' %}",
        "tags": ["art", "drawing", "sketching", "painting", "illustrating", "beautiful", "artist", "watercolor", "watercolour"]
    },
    {
        "title": "Math",
        "image": "{% static 'password_dashboard/cathegories_images/math.svg' %}",
        "tags": ["math", "algebra", "geometry", "science", "school", "equation"]
    },
    {
        "title": "Language",
        "image": "{% static 'password_dashboard/cathegories_images/language.svg' %}",
        "tags": ["language", "school", "albanian", "american", "arabic", "armenian", "british", "bulgarian", "chinese", "czech", "dutch", "egyptian", "english", "estonian", "french", "german", "georgian", "greek", "hawaiian", "hindi", "indonesian", "iraqw", "irish", "italian", "japanese", "kannada", "korean", "mongolic", "nigerian", "polish", "portuguese", "russian", "romanian", "serbian", "slavic", "spanish", "taiwanese", "turkish", "ukrainian", "vietnamese"]
    },
    {
        "title": "Science",
        "image": "{% static 'password_dashboard/cathegories_images/science.svg' %}",
        "tags": ["science", "math", "physics", "chemistry", "biology", "engineering", "mechanical", "electrical", "computer"]
    },
    {
        "title": "Robotics",
        "image": "{% static 'password_dashboard/cathegories_images/robotics.svg' %}",
        "tags": ["robotics", "robot", "engineering", "mechanical", "electrical", "computer", "arduino", "raspberry", "pi", "raspberripi"]
    },
    {
        "title": "Dancing",
        "image": "{% static 'password_dashboard/cathegories_images/dancing.svg' %}",
        "tags": ["dancing", "dance", "beauty", "beautiful", "choreography", "balley", "modern", "samba", "tap", "folk", "salsa", "hip", "hop", "hiphop", "acrobatic", "tango", "capoeira"]
    },
    {
        "title": "Music / Singing",
        "image": "{% static 'password_dashboard/cathegories_images/music_singing.svg' %}",
        "tags": ["singing", "song", "beautiful", "musician", "singer", "art", "rock", "jazz", "disco", "hip", "hop", "hiphop", "electronic", "folk", "funk", "heavy", "metal"]
    },
    {
        "title": "Video games",
        "image": "{% static 'password_dashboard/cathegories_images/video_games.svg' %}",
        "tags": ["video", "games", "videogames", "console", "pc", "computer", "pvp", "online", "offline", "arcade"]
    },
    {
        "title": "Yoga / Mediatation",
        "image": "{% static 'password_dashboard/cathegories_images/yoga_meditation.svg' %}",
        "tags": ["yoga", "meditation", "relax", "exercise", "peace", "pilates", "workout", "mind"]
    },
    {
        "title": "Martial arts",
        "image": "{% static 'password_dashboard/cathegories_images/martial_arts.svg' %}",
        "tags": ["martial", "arts", "kung", "fu", "kungfu", "taekwondo", "karate", "kickboxing", "hapkido", "aikido", "judo"]
    },
    {
        "title": "Design",
        "image": "{% static 'password_dashboard/cathegories_images/design.svg' %}",
        "tags": ["design", "illustrating", "drawing", "sketching", "modern", "art", "artist", "digital"]
    },
    {
        "title": "School / University",
        "image": "{% static 'password_dashboard/cathegories_images/school_university.svg' %}",
        "tags": ["school", "university", "colleague", "degree", "master", "science", "profession"]
    },
].sort((a, b) => a.title.localeCompare(b.title));

console.log(abc);


let cathegory_value = '';

            cathegory_input_hidden.value = "Hello";
            // console.log(cathegory_input_hidden.value);



function examinInput() {
    value = cathegories_input.value;
    if (value.trim() == '') {
        cathegories_input.value = '';
        load_cathegories(abc)
    } else {
        searchTags(value);
    }
}

function load_cathegories(abc) {
    
    var cathegories_list_content = "";
    for (i = 0; i < abc.length; i++) {
        cathegories_list_content += `<li><img src="${abc[i].image}"><p>${abc[i].title}</p></li>`;
    }
    cathegories_list.querySelector("span").innerHTML = cathegories_list_content;
    cathegories_list = document.querySelector("#cathegories_wrapper");
    handleCathegoriesClicking();
}



function searchTags(value) {
    found_indexes = [];
    input_arr = value.trim().split(' ');
    newCathegories = [];
    for (i = 0; i < input_arr.length; i++) {
        if (input_arr[i] == '') {
            input_arr.splice(i, 1);
        }
    }
    for (k = 0; k < input_arr.length; k++) {
        for (i = 0; i < abc.length; i++) {
            for (j = 0; j < abc[i].tags.length; j++) {
                if (abc[i].tags[j].toLowerCase().includes(input_arr[k].toLowerCase())) {
                    if (!found_indexes.includes(i)) {
                        found_indexes.push(i);
                    }
                }
            }
        }
    }
    for (i = 0; i < found_indexes.length; i++) {
        newCathegories.push(abc[found_indexes[i]]);
    }
    load_cathegories(newCathegories);
}

// function handlePlaceholder() {
//     window.addEventListener("mousedown", (e) => {
//         body = document.querySelector("body");
//         container = document.querySelector("#container");
//         if (e.target == body || e.target == container) {
//             cathegories_placeholder.classList.remove("hide_placeholder");
//         } else {
//             cathegories_placeholder.classList.add("hide_placeholder");
//         }
//     })
// }


function handleCathegoriesClicking() {
    cathegories_list.querySelectorAll("li").forEach((this_item) => {
        this_item.addEventListener("click", () => {
            cathegories_input.classList.add("hide_placeholder");
            image_src = this_item.querySelector("img").getAttribute("src");
            title = this_item.querySelector("p").textContent;
            current_cathegory.querySelector("div img").setAttribute("src", image_src);
            current_cathegory.querySelector("div p").textContent = title;
            cathegories_input.value = title;
            cathegory_input_hidden.value = title;
            console.log(cathegory_input_hidden.value);
            
            current_cathegory.classList.add("show_current_cathegory");
            if (input_field[0].querySelector("input").value.trim() != '') {
                generate.classList.add("generate_on");
            }
        });
    })
}

cathegories_input.addEventListener("focus", () => {
    cathegories_list.classList.add("show_cathegories_list");
    examinInput()
    cathegories_list.scrollTop = 0;
    cathegories_placeholder.classList.add("hide_placeholder");
});

cathegories_input.addEventListener("blur", () => {
    cathegories_list.classList.remove("show_cathegories_list");
    if (cathegories_input.value.trim() != '') {
        cathegories_placeholder.classList.add("hide_placeholder");
    } else {
        cathegories_placeholder.classList.add("hide_placeholder");
        setTimeout(() => {
            cathegories_placeholder.classList.remove("hide_placeholder");

        }, 300)

        // handlePlaceholder();
    }
});


// handlePlaceholder();


cathegories_input.addEventListener("keypress", (e) => {
    if (e.key == ',') {
        e.preventDefault();
    }
})

cathegories_input.addEventListener("input", () => {

    examinInput()
});

remove_cathegory.addEventListener("click", () => {
    cathegories_input.value = '';
    current_cathegory.classList.remove("show_current_cathegory");
    cathegories_input.focus();
    cathegory_value = '';
    generate.classList.remove("generate_on");
})