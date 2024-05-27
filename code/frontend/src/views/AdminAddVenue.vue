<template>
	<div class="add-venue">
		<div class="venue">
			<div class="venue-form">
				<div class="venue-form-header">Add a venue</div>
				<div class="venue-form-body">
					<validation-observer v-slot="{ invalid, handleSubmit }">
						<form @submit.prevent="handleSubmit(submitVenue)">
							<div class="form-group">
								<label for="venue_name">Name</label>
								<validation-provider
									rules="required|min:3|max:20"
									v-slot="{ errors }"
								>
									<input
										type="text"
										id="venue_name"
										v-model="venue_name"
										placeholder="Enter the venue name"
									/>
									<div class="text-danger push-right">
										{{ errors[0] }}
									</div>
								</validation-provider>
							</div>
							<div class="form-group">
								<label for="venue_state">State</label>
								<validation-provider
									rules="required|min:3|max:20"
									v-slot="{ errors }"
								>
									<input
										type="text"
										id="venue_state"
										v-model="venue_state"
										placeholder="Enter the venue state"
									/>
									<div class="text-danger push-right">
										{{ errors[0] }}
									</div>
								</validation-provider>
							</div>
							<div class="form-group">
								<label for="venue_city">City</label>
								<validation-provider
									rules="required|min:3|max:20"
									v-slot="{ errors }"
								>
									<input
										type="text"
										id="venue_city"
										v-model="venue_city"
										placeholder="Enter the venue city"
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
								>Add Venue</b-button
							>

							<b-modal
								v-model="show"
								id="add-venue"
								title="Confirm venue addition"
							>
								<p class="my-4">Are your sure you want to add this venue?</p>
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
										@click="submitVenue(movie)"
									>
										Add Venue
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
import { mapGetters, mapActions } from 'vuex';
import { ValidationProvider, ValidationObserver } from 'vee-validate';

export default {
	name: 'AddVenue',
	data() {
		return {
			venue_name: '',
            venue_state: '',
            venue_city: '',
			show: false
		};
	},
	components: {
		ValidationObserver,
		ValidationProvider,
	},
	methods: {
		...mapGetters(['getAccessToken']),
		...mapActions(['loadVenue']),
		async submitVenue() {
			const venueData = {
				venue_name: this.venue_name,
				venue_state: this.venue_state,
				venue_city: this.venue_city,
			};
			await axios
				.post('http://localhost:5000/adminaddvenue', venueData, {
					headers: {
						'Content-Type': 'application/json',
						Authorization: `Bearer ${this.getAccessToken()}`
					},
				})
				.then(() => {
					alert('Venue added successfully!');
					this.$router.push(`/adminvenue`);
				})
				.catch(() => {
					alert('Error adding venue!');
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
.venue {
	display: flex;
	justify-content: center;
	align-items: center;
	padding: 20px 0 40px 0;
	background-color: #f5f5f5;
}
.venue-form {
	padding: 50px 200px;
}
.venue-form-header {
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
