<template>
	<div class="modify-venue">
		<div class="modify-venue-form">
			<div class="modify-venue-form-header">
				Update the details of the venue
			</div>
			<div class="modify-venue-form-body">
				<validation-observer v-slot="{ invalid, handleSubmit }">
					<form @submit.prevent="handleSubmit(saveVenue)">
						<div class="form-group">
							<label for="name">Name</label>
							<validation-provider
								rules="required|min:3|max:20"
								v-slot="{ errors }"
							>
								<input
                                    type="text"
									id="venue_name"
									v-model="localVenue.venue_name"
									:disabled="isDisabled"
									placeholder="Enter the name of the venue"
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
                                    v-model="localVenue.venue_state"
									:disabled="isDisabled"
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
									v-model="localVenue.venue_city"
									placeholder="Enter the venue city"
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
								Update Venue
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
							id="venue-modify-confirm"
							title="Confirm Venue Modification"
						>
							<p class="my-4">Are your sure you want to save this venue?</p>
							<template #modal-footer>
								<b-button
									size="md"
									class="float-right btn-red"
									@click="resetVenue()"
								>
									Reset
								</b-button>
								<b-button
									size="md"
									class="float-right btn-yellow"
									@click="saveVenue()"
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
import { mapGetters } from 'vuex';
import { ValidationProvider, ValidationObserver } from 'vee-validate';
import axios from 'axios';

export default {
	name: 'ModifyVenue',
	data() {
		return {
			localVenue: {
				venue_name: '',
                venue_state: '',
                venue_city: '',
			},
			dummyVenue: {}, // dummyVenue is used to check if the user has changed any of the fields
			isDisabled: true,
			show: false,
		};
	},
	components: {
		ValidationObserver,
		ValidationProvider,
	},
	computed: {
		...mapGetters(['getVenue', 'getAdminID', 'getAccessToken']),
	},
	async beforeMount() {
		this.localVenue = this.getVenue;
	},
	mounted() {
		this.dummyVenue = {
			venue_id: this.localVenue.venue_id,
			venue_name: this.localVenue.venue_name,
            venue_state: this.localVenue.venue_state,
            venue_city: this.localVenue.venue_city,
		};
	},
	methods: {
		resetVenue() {
			this.localVenue = this.dummyVenue;
			this.isDisabled = true;
			this.show = false;
		},
		checkUpdate() {
			if (
				this.localVenue.venue_id !== this.dummyVenue.venue_id ||
				this.localVenue.venue_name !== this.dummyVenue.venue_name ||
				this.localVenue.venue_state !== this.dummyVenue.venue_state ||
				this.localVenue.venue_city !== this.dummyVenue.venue_city
			) {
				return true;
			}
			return false;
		},
		async saveVenue() {
			if (this.checkUpdate()) {
				const venueData = {
					venue_name: this.localVenue.venue_name,
					venue_state: this.localVenue.venue_state,
					venue_city: this.localVenue.venue_city,
				};
				await axios
					.put(
						`http://localhost:5000/modifyvenue/${this.$route.params.venue_id}`,
						venueData,
						{
							headers: {
								'Content-Type': 'application/json',
								Authorization: `Bearer ${this.getAccessToken}`
							},
						},
					)
					.then(() => {
						alert('Venue updated successfully');
					})
					.catch(() => {
						alert('Error updating venue');
					});
			}
			this.show = false;
			this.isDisabled = true;
		},
	},
};
</script>

<style scoped>
.modify-venue {
	display: flex;
	justify-content: center;
	align-items: center;
	margin: 50px 0 100px 0;
}
.modify-venue-form {
	background-color: #f5f5f5;
	padding: 50px 200px;
}
.modify-venue-form-header {
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
