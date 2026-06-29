from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary in-memory database of cars
cars_db = [
    {"id": 1, "make": "Toyota", "model": "Corolla", "year": 2022, "price": 22000, "image": "https://unsplash.com"},
    {"id": 2, "make": "Tesla", "model": "Model 3", "year": 2023, "price": 40000, "image": "https://unsplash.com"},
    {"id": 3, "make": "Ford", "model": "Mustang", "year": 2021, "price": 36000, "image": "https://unsplash.com"}
]

@app.route('/')
def home():
    # Displays all cars on the homepage
    return render_template('index.html', cars=cars_db)

@app.route('/car/<int:car_id>')
def car_detail(car_id):
    # Finds a specific car by its ID number
    car = next((c for c in cars_db if c['id'] == car_id), None)
    if car is None:
        return "Car not found", 404
    return render_template('detail.html', car=car)

@app.route('/add', methods=['GET', 'POST'])
def add_car():
    # Handles both viewing the form and submitting new car data
    if request.method == 'POST':
        new_car = {
            "id": len(cars_db) + 1,
            "make": request.form['make'],
            "model": request.form['model'],
            "year": int(request.form['year']),
            "price": int(request.form['price']),
            "image": request.form['image'] or "https://unsplash.com"
        }
        cars_db.append(new_car)
        return redirect(url_for('home'))
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
