<html>
<label for="weather">Select the weather</label>
<select id="weather">
        <option value="">--Make a choice--</option>
        <option value="sunny">Sunny</option>
        <option value="rainy">Rainy</option>
        <option value="snowing">Snowing</option>
        <option value="overcast">Overcast</option>
</select>
<p></p>
const select = document.querySelector('select');
const para = document.querySelector('p');

select.addEventListener('change', setWeather);

function setWeather() {
    const choice = select.value;

    if (choice == 'sunny') {
        para.context = ''
    }
}
    
</html>
