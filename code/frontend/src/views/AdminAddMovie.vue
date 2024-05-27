<template>
	<div class="add-movie">
		<div class="movie">
			<div class="movie-form">
				<div class="movie-form-header">Add a movie</div>
				<div class="movie-form-body">
					<validation-observer v-slot="{ invalid, handleSubmit }">
						<form @submit.prevent="handleSubmit(submitMovie)">
							
							<div class="form-group">
							<label for="name">Name</label>
							<validation-provider
								rules="required|min:3|max:30"
								v-slot="{ errors }"
							>
								<input
									type="text"
									id="name"
									v-model="name"
									placeholder="Enter the name of the movie"
								/>
								<div class="text-danger push-right">
									{{ errors[0] }}
								</div>
							</validation-provider>
							</div>
							<div class="form-group">
								<label for="movie_rating">Rating</label>
								<validation-provider
									v-slot="{ errors }"
								>
									<input
										type="number"
										id="movie_rating"
										v-model="movie_rating"
										placeholder="Enter the movie rating"
									/>
									<div class="text-danger push-right">
										{{ errors[0] }}
									</div>
								</validation-provider>
							</div>
							<div class="form-group">
								<label for="movie_time">Movie Time</label>
								<validation-provider
								rules="required|min:3|max:50"
									v-slot="{ errors }"
								>
									<input
										type="datetime-local"
										id="movie_time"
										v-model="movie_time"
										placeholder="Enter the movie timing"
									/>
									<div class="text-danger push-right">
										{{ errors[0] }}
									</div>
								</validation-provider>
							</div>
							<div class="form-group">
								<label for="category">Category</label>
								<validation-provider rules="required" v-slot="{ errors }">
									<select id="category" v-model="category_id">
										<option value="" disabled>Select a category</option>
										<option
											v-for="(category, idx) in categories"
											:value="category"
											:key="idx"
										>
											{{ category.category_id + ' - ' + category.name }}
										</option>
									</select>
									<div class="text-danger push-right">
										{{ errors[0] }}
									</div>
								</validation-provider>
							</div>
							<div class="form-group">
								<label for="ticket_price">Ticket Price</label>
								<validation-provider
									rules="required|min_value:100|max_value:99999999"
									v-slot="{ errors }"
								>
									<input
										type="numeric"
										id="ticket_price"
										v-model="ticket_price"
										placeholder="Enter the price of one ticket"
									/>
									<div class="text-danger push-right">
										{{ errors[0] }}
									</div>
								</validation-provider>
							</div>
							<div class="form-group">
								<label for="number_of_seats">Number of Seats</label>
								<validation-provider
									rules="required|min_value:50|max_value:99999999"
									v-slot="{ errors }"
								>
									<input
										type="numeric"
										id="number_of_seats"
										v-model="number_of_seats"
										placeholder="Enter the number of seats present for this movie"
									/>
									<div class="text-danger push-right">
										{{ errors[0] }}
									</div>
								</validation-provider>
							</div>
							<b-button
								@click="show = true"
								:disabled="invalid"
								class="btn btn-yellow push-right"
								>Add Movie</b-button
							>

							<b-modal
								v-model="show"
								id="add-movie"
								title="Confirm movie addition"
							>
								<p class="my-4">Are your sure you want to add this movie?</p>
								<template #modal-footer>
									<b-button
										size="md"
										class="float-right btn btn-red"
										@click="show = false"
									>
										Cancel
									</b-button>
									<b-button
										size="md"
										class="float-right btn btn-yellow"
										@click="submitMovie"
									>
										Add Movie
									</b-button>
								</template>
							</b-modal>
						</form>
					</validation-observer>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import axios from 'axios';
import { mapActions, mapGetters } from 'vuex';
import { ValidationProvider, ValidationObserver } from 'vee-validate';

export default {
	name: 'AddMovie',
	props:['venue_id'],
	data() {
		return {
			name: '',
			movie_rating: '',
			movie_time:'',
			category_id: '',
			ticket_price:'',
			number_of_seats:'',
			show: false,
			categories: {},
		};
	},
	components: {
		ValidationObserver,
		ValidationProvider,
	},
	created(){
		let response = fetch ("http://localhost:5000/admincategories",
			{method: "GET",
				headers: {
				'Content-Type': 'application/json',
				Authorization: `Bearer ${this.getAccessToken()}`}}).then(x=>x.json())
			response.then(x=> {this.categories =x; console.log (x)})
	},
	methods: {
		...mapGetters(['getAccessToken']),
		...mapActions(['loadMovie']),
		async submitMovie() {
			const movieData = {
				name: this.name,
				venue_id: this.venue_id,
				movie_rating: this.movie_rating,
				movie_time: this.movie_time,
				category_id: this.category_id["category_id"],
				ticket_price: this.ticket_price,
				number_of_seats: this.number_of_seats,
			};
			await axios
				.post('http://localhost:5000/adminaddmovie', movieData, {
					headers: {
						'Content-Type': 'application/json',
						Authorization: `Bearer ${this.getAccessToken()}`,
					},
				})
				.then(() => {
					alert('Movie added successfully!');
					this.$router.push(`/adminmovie/${this.venue_id}`);
				})
				.catch(() => {
					alert('Error adding movie!');
				});
		},
	},
};
</script>

<style scoped>
.banner-container {
	position: relative;
}
.banner {
	width: 100%;
}
.heading {
	font-size: 3.5rem;
	font-weight: bold;
	color: #fff;
}
.text {
	font-size: 3rem;
	color: #eee;
	font-weight: 600;
	margin-top: 10px;
}
/* Form */
.movie {
	display: flex;
	justify-content: center;
	align-items: center;
	padding: 20px 0 40px 0;
	background-color: #f5f5f5;
}
.movie-form {
	padding: 50px 200px;
}
.movie-form-header {
	font-size: 36px;
	font-weight: bold;
	margin-bottom: 70px;
	text-align: center;
}
label {
	width: 150px;
	font-weight: 500;
}
.form-group {
	margin-bottom: 30px;
}
select {
	width: 600px;
	height: 35px;
	border: 1px solid #eee;
	padding: 0 10px;
}
input {
	width: 400px;
	height: 35px;
	border: 1px solid #eee;
	padding: 0 10px;
}
textarea {
	width: 600px;
	height: 100px;
	border: 1px solid #eee;
	padding: 10px;
	resize: none;
}
.textarea-label {
	vertical-align: top;
}
.btn-yellow {
	background-color: #e4c314 !important;
	color: #000 !important;
	font-weight: 600;
}
.btn-yellow:disabled {
	background-color: #666 !important;
	color: #fff !important;
}
.btn-red {
	background-color: #ff918d !important;
	color: #000 !important;
	font-weight: 600;
}
.push-right {
	margin-left: 150px;
}
</style>
