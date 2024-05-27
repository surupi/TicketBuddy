<template>
	<div class="modify-movie">
		<div class="modify-movie-form">
			<div class="modify-movie-form-header">
				Update the details of the movie
			</div>
			<div class="modify-movie-form-body">
				<validation-observer v-slot="{ invalid, handleSubmit }">
					<form @submit.prevent="handleSubmit(saveMovie)">
						<div class="form-group">
							<label for="name">Name</label>
							<validation-provider
								rules="required|min:3|max:30"
								v-slot="{ errors }"
							>
								<input
									type="text"
									id="name"
									v-model="localMovie.name"
									:disabled="isDisabled"
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
										v-model="localMovie.movie_rating"
										:disabled="isDisabled"
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
										v-model="localMovie.movie_time"
                                        :disabled="isDisabled"
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
									<select id="category" v-model="localMovie.category_id" :disabled="isDisabled">
										<option value="" disabled>Select a category</option>
										<option
											v-for="(category, idx) in categories"
											:value="category.category_id"
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
										v-model="localMovie.ticket_price"
                                        :disabled="isDisabled"
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
										v-model="localMovie.number_of_seats"
                                        :disabled="isDisabled"
										placeholder="Enter the number of seats present for this movie"
									/>
									<div class="text-danger push-right">
										{{ errors[0] }}
									</div>
								</validation-provider>
						</div>

						<div>
							<button
								v-if="isDisabled === true"
								class="btn btn-yellow push-right"
								@click.prevent="isDisabled = false"
							>
								Update Movie
							</button>
							<b-button
								v-else
								@click="show = true"
								class="btn-bg btn-yellow push-right"
								:disabled="invalid"
								>Save</b-button
							>
						</div>

						<b-modal
							v-model="show"
							id="movie-modify-confirm"
							title="Confirm Movie Modification"
						>
							<p class="my-4">Are your sure you want to save this movie?</p>
							<template #modal-footer>
								<b-button
									size="md"
									class="float-right btn-red"
									@click="resetMovie()"
								>
									Reset
								</b-button>
								<b-button
									size="md"
									class="float-right btn-yellow"
									@click="saveMovie()"
								>
									Save
								</b-button>
							</template>
						</b-modal>
					</form>
				</validation-observer>
			</div>
		</div>
	</div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import { ValidationProvider, ValidationObserver } from 'vee-validate';
import axios from 'axios';

export default {
	name: 'ModifyMovie',
	data() {
		return {
			localMovie: {
				name: '',
				movie_rating: '',
				movie_time:'',
				category_id: '',
				ticket_price:'',
				number_of_seats:'',
				show: false,
				categories: {},
			},
			dummyMovie: {}, // dummyMovie is used to check if the user has changed any of the fields
			isDisabled: true,
			show: false,
			categories: []
		};
	},
	created(){
		this.loadMovie()
		this.loadCategories()
	},
	components: {
		ValidationObserver,
		ValidationProvider,
	},
	computed: {
		...mapGetters(['getMovie', 'getAdminID', 'getAccessToken', 'getCategories']),
	},

	async beforeMount() {
		
		this.localMovie = this.$store.state.movie;
		this.categories = this.$store.state.categories;

	},
	mounted() {
		this.dummyMovie = {
			movie_id: this.localMovie.movie_id,
			name: this.name,
			venue_id: this.venue_id,
			movie_rating: this.movie_rating,
			movie_time: this.movie_time,
			category_id: this.category_id,
			ticket_price: this.ticket_price,
			number_of_seats: this.number_of_seats,
		};
	},
	methods: {
		...mapActions(["loadMovie", "loadCategories"]),
		resetMovie() {
			this.localMovie = this.dummyMovie;
			this.isDisabled = true;
			this.show = false;
		},
		checkUpdate() {
			if (
				this.localMovie.movie_id !== this.dummyMovie.movie_id ||
				this.localMovie.name !== this.dummyMovie.name ||
				this.localMovie.venue_id !== this.dummyMovie.venue_id ||
				this.localMovie.movie_rating !== this.dummyMovie.movie_rating ||
				this.localMovie.movie_time !== this.dummyMovie.movie_time ||
				this.localMovie.category_id !== this.dummyMovie.category_id ||
				this.localMovie.ticket_price !== this.dummyMovie.ticket_price ||
				this.localMovie.number_of_seats !== this.dummyMovie.number_of_seats
			) {
				return true;
			}
			return false;
		},
		async saveMovie() {
			if (this.checkUpdate()) {
				const movieData = {
					name: this.localMovie.name,
					venue_id: this.localMovie.venue_id,
					movie_rating: this.localMovie.movie_rating,
					movie_time: this.localMovie.movie_time,
					category_id: this.localMovie.category_id,
					ticket_price: this.localMovie.ticket_price,
					number_of_seats: this.localMovie.number_of_seats,
				};
				await axios
					.put(
						`http://localhost:5000/modifymovie/${this.$route.params.movie_id}`,
						movieData,
						{
							headers: {
								'Content-Type': 'application/json',
								Authorization: `Bearer ${this.getAccessToken}`
							},
						},
					)
					.then(() => {
						alert('Movie updated successfully');
					})
					.catch(() => {
						alert('Error updating movie');
					});
			}
			this.show = false;
			this.isDisabled = true;
		},
	},
};
</script>

<style scoped>
.modify-movie {
	display: flex;
	justify-content: center;
	align-items: center;
	margin: 50px 0 100px 0;
}
.modify-movie-form {
	background-color: #f5f5f5;
	padding: 50px 200px;
}
.modify-movie-form-header {
	font-size: 36px;
	font-weight: bold;
	margin-bottom: 50px;
	text-align: center;
}
label {
	width: 150px;
	font-weight: 500;
}
.form-group {
	margin-bottom: 30px;
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
.push-right {
	margin-left: 150px;
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
	background-color: #ff918d;
	color: #000;
	font-weight: 600;
}
input:disabled {
	background-color: #dfdfdf;
}
textarea:disabled {
	background-color: #dfdfdf;
}
</style>
