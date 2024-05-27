<template>
	<div class="add-booking">
		<div class="booking">
			<div class="booking-form">
				<div class="booking-form-header">Book tickets for this movie</div>
				<div class="booking-form-body">
					<validation-observer v-slot="{ invalid, handleSubmit }">
						<form @submit.prevent="handleSubmit(submitBooking)">
                            <div class="form-group">
								<label for="Booking">Number of tickets</label>
								<validation-provider
									v-slot="{ errors }"
								>
									<input
										type="number"
										id="number_of_tickets"
										v-model="number_of_tickets"
										placeholder="Number of tickets you want to book for this movie"
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
								>Add Booking</b-button
							>

							<b-modal
								v-model="show"
								id="add-booking"
								title="Confirm booking addition"
							>
								<p class="my-4">Are your sure you want to add this booking?</p>
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
										@click="submitBooking"
									>
										Add Booking
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
import { mapActions, mapGetters} from 'vuex';
import { ValidationProvider, ValidationObserver } from 'vee-validate';

export default {
	name: 'AddBooking',
	data() {
		return {
			number_of_tickets: '',
			show: false,
		};
	},
	components: {
		ValidationObserver,
        ValidationProvider,
	},
	methods: {
		...mapActions(['loadBooking']),
		...mapGetters(['getAccessToken']),
		async submitBooking() {
			const bookingData = {
				number_of_tickets: this.number_of_tickets,
			};
			console.log(`${this.$route.params.movie_id}`)
			await axios
				.post(`http://localhost:5000/useraddbooking/${this.$route.params.movie_id}`, bookingData, {
					headers: {
						'Content-Type': 'application/json',
						Authorization: `Bearer ${this.getAccessToken()}`
					},
				})
				
				.then((response) => {
					alert(response.data["message"]);
					this.$router.push(`/useraddbooking`);
				})
				.catch(() => {
					alert('Error adding booking!');
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
.booking {
	display: flex;
	justify-content: center;
	align-items: center;
	padding: 20px 0 40px 0;
	background-color: #f5f5f5;
}
.booking-form {
	padding: 50px 200px;
}
.booking-form-header {
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
