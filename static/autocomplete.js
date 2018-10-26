
function autocomplete(inp, arr) {
  /*the autocomplete function takes two arguments,
  the text field element and an array of possible autocompleted values:*/
  var currentFocus;
  /*execute a function when someone writes in the text field:*/
  inp.addEventListener("input", function(e) {
      var a, b, i, val = this.value;
      /*close any already open lists of autocompleted values*/
      closeAllLists();
      if (!val) { return false;}
      currentFocus = -1;
      /*create a DIV element that will contain the items (values):*/
      a = document.createElement("DIV");
      a.setAttribute("id", this.id + "autocomplete-list");


      a.setAttribute("class", "autocomplete-items");
      /*append the DIV element as a child of the autocomplete container:*/
      this.parentNode.appendChild(a);

     var j = 0;
      /*for each item in the array...*/
      for (i = 0; i < arr.length; i++) {
        /*check if the item starts with the same letters as the text field value:*/
        if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
          /*create a DIV element for each matching element:*/
          b = document.createElement("DIV");
          /*make the matching letters bold:*/

          b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
          b.innerHTML += arr[i].substr(val.length);
          /*insert a input field that will hold the current array item's value:*/
          b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
          j++;
          /*execute a function when someone clicks on the item value (DIV element):*/
          b.addEventListener("click", function(e) {
              /*insert the value for the autocomplete text field:*/
              inp.value = this.getElementsByTagName("input")[0].value;

                  /*close the list of autocompleted values,
              (or any other open lists of autocompleted values:*/
              closeAllLists()

          });

          if(j>5){
              a.style.height = '200px';
              a.style.overflowY = 'scroll';
          }
          a.appendChild(b);
        }
      }
  });
  /*execute a function presses a key on the keyboard:*/
  inp.addEventListener("keydown", function(e) {
      var x = document.getElementById(this.id + "autocomplete-list");
      if (x) x = x.getElementsByTagName("div");
      if (e.keyCode == 40) {
        /*If the arrow DOWN key is pressed,
        increase the currentFocus variable:*/
        currentFocus++;
        /*and and make the current item more visible:*/
        addActive(x);
      } else if (e.keyCode == 38) { //up
        /*If the arrow UP key is pressed,
        decrease the currentFocus variable:*/
        currentFocus--;
        /*and and make the current item more visible:*/
        addActive(x);
      } else if (e.keyCode == 13) {
        /*If the ENTER key is pressed, prevent the form from being submitted,*/
        e.preventDefault();
        if (currentFocus > -1) {
          /*and simulate a click on the "active" item:*/
          if (x) x[currentFocus].click();
        }
      }
  });
  function addActive(x) {
    /*a function to classify an item as "active":*/
    if (!x) return false;
    /*start by removing the "active" class on all items:*/
    removeActive(x);
    if (currentFocus >= x.length) currentFocus = 0;
    if (currentFocus < 0) currentFocus = (x.length - 1);
    /*add class "autocomplete-active":*/
    x[currentFocus].classList.add("autocomplete-active");
  }
  function removeActive(x) {
    /*a function to remove the "active" class from all autocomplete items:*/
    for (var i = 0; i < x.length; i++) {
      x[i].classList.remove("autocomplete-active");
    }
  }
  function closeAllLists(elmnt) {
    /*close all autocomplete lists in the document,
    except the one passed as an argument:*/
    var x = document.getElementsByClassName("autocomplete-items");
    for (var i = 0; i < x.length; i++) {
      if (elmnt != x[i] && elmnt != inp) {
        x[i].parentNode.removeChild(x[i]);
      }
    }
  }
  /*execute a function when someone clicks in the document:*/
  document.addEventListener("click", function (e) {
      closeAllLists(e.target);
  });
}

/*An array containing all the suburb names in the DB:*/
var countries = ['Mosman', 'Elanora Heights', 'Allambie Heights', 'Tamarama', 'Bondi Beach', 'Sydney', 'Pyrmont', 'Potts Point', 'Balgowlah', 'Bondi Junction', 'Randwick', 'North Ryde', 'Byron Bay', 'North Bondi', 'North Curl Curl', 'Coogee', 'Ultimo', 'Surry Hills', 'Rose Bay', 'Zetland', 'Arncliffe', 'Carnes Hill', 'Sans Souci', 'Chiswick', 'Manly', 'Elizabeth Bay', 'Rockdale', 'Chippendale', 'Bronte', 'Camperdown', 'Bondi', 'Darlinghurst', 'Wolli Creek', 'Erskineville', 'Waterloo', 'Redfern', 'Wollstonecraft', 'Waverton', 'Suffolk Park', 'Double Bay', 'Kingsford', 'Campsie', 'Clovelly', 'Neutral Bay', 'Maroubra', 'Rushcutters Bay', 'Newtown', 'Bellevue Hill', 'Davidson', 'Waverley', 'Paddington', 'Hunters Hill', 'Frenchs Forest', 'Kensington', 'Cherrybrook', 'Narrabeen', 'Watsons Bay', 'Merrylands', 'Strathfield', 'West Pymble', 'Marrickville', 'Annandale', 'Manly Vale', 'Ashfield', 'Woolloomooloo', 'West Pennant Hills', 'Kingscliff', 'Mullumbimby', 'Lane Cove', 'Drummoyne', 'Rose bay', 'Petersham', 'Newport', 'Beaconsfield', 'Parramatta', 'Chatswood', 'Campbelltown', 'Tweed Heads South', 'Darlinghurst - Sydney', 'North Sydney', 'Liverpool', 'Burwood', 'Granville', 'Harrington Park', 'Brooklet', 'Avalon Beach', 'Edgecliff', 'Macquarie Park', 'Stanmore', 'Edensor Park', 'Pendle Hill', 'Berowra', 'Leichhardt', 'Fairlight', 'Eastwood', 'Rozelle', 'Ryde', 'Carlingford', 'Berowra Waters', 'Angourie', 'Queens Park', 'Auburn', 'Allawah', 'Gladesville, New South Wales, AU', 'Artarmon', 'Tintenbar', 'Billinudgel', 'Homebush West', 'Ballina', 'Menai', 'Sydney Olympic Park', 'Dover Heights', 'Cremorne', 'Waitara', 'Ocean Shores', 'Darlington', 'Hurstville', 'Toongabbie', 'Alexandria', 'St Peters /Newtown', 'Belmore', 'Baulkham Hills', 'Willoughby', 'Yamba', 'Palm Beach', 'Millers Point', 'Marsfield', 'Maclean', 'McMahons Point', 'Warriewood', 'Burraneer', 'Darling Point', 'Emu Plains', 'East Killara', 'North Manly', 'Enmore', 'Croydon Park', 'Mount Annan', 'Cumbalum', 'Birchgrove', 'Brooklyn', 'Pymble', 'Lavender Bay', 'Lennox Head', 'Bangalow', 'Woollahra', 'Federal', 'Loftus', 'Bella Vista', 'Dee Why', 'Botany', 'Coorabell', 'Bexley North', 'New Brighton', 'Rosebery', 'Abbotsford', 'Holroyd', 'Meadowbank', 'Lindfield', 'Nimbin', 'Cammeray', 'Lewisham', 'Dulwich Hill', 'Wadeville', 'Wilsons Creek', 'Casuarina', 'Mona Vale', 'Epping', 'Stokers Siding', 'Haberfield', 'Queenscliff', 'Queens park', 'Milsons Point', 'Cremorne Point', 'Tyringham', 'North Narrabeen', 'Caringbah', 'Glebe', 'Wooli', 'Beverly Hills', 'Blacktown', 'Haymarket', 'Forestville', 'Dangar Island', 'Bellevue hill', 'The Pocket', 'Broken Head', 'Freshwater', 'Ermington', 'Mascot', 'Banksia', 'Wheeler Heights', 'Lilyfield', 'Saint Peters', 'Brunswick Heads', 'Centennial Park', 'Spencer', 'Enfield', 'North Curl Curl (near Manly)', 'Balmain', 'Croydon', 'Beacon Hill', 'Concord West', 'East Lindfield', 'Hillsdale', 'Clareville', 'Lane Cove West', 'The Ponds', 'Kogarah', 'Forest Lodge', 'Newington', 'Main Arm', 'Padstow', 'Wooloweyah', 'Naremburn', 'Rhodes', 'Pennant Hills', 'Wentworth Point', 'Arcadia', 'Edmondson Park', 'Five Dock', 'Newrybar', 'Crows Nest', 'Scotland Island', 'Greenwich', 'Little Bay', 'Beecroft', 'Vaucluse', 'Balgowlah Heights', 'Girards Hill', 'Uki', 'Summer Hill', 'Kirribilli', 'Hornsby Heights', 'Lismore', 'Henley', 'Kurraba Point', 'Wareemba', 'Wollstonecraft, Sydney', 'South Coogee', 'Cronulla', 'Bondi junction', 'Iluka', 'St Peters', 'Ramsgate Beach', 'Brookvale', 'Westmead', 'Matraville', 'North Balgowlah', 'Palmers Island', 'Northbridge', 'Pottsville', 'Myocum', 'Collaroy Plateau', 'Homebush', 'Lovett Bay', 'Malabar', 'Carlton', 'Council of the City of Sydney', 'Collaroy', 'Talofa', 'Binna Burra', 'Balmain East', 'Rosehill', 'Saint Leonards', 'Canterbury', 'Bondi beach', 'Rosebank', 'Rukenvale', 'Miranda', 'Tyalgum', 'St Leonards', 'Tweed Heads', 'South Turramurra']
/*initiate the autocomplete function on the "myInput" element, and pass along the countries array as possible autocomplete values:*/
