<template>
	<div class="profile">
		<div class="profile-form">
			<div class="profile-form-header">Your profile</div>
			<div class="profile-form-body">
				<validation-observer v-slot="{ invalid }">
					<form @submit.prevent="saveProfile">
						<div class="form-group">
							<label for="name">Name</label>
							<validation-provider
								rules="required|min:3|max:30"
								v-slot="{ errors }"
							>
								<input
									type="text"
									id="name"
									v-model="localUser.name"
									:disabled="isDisabled"
									placeholder="Enter your name"
								/>
								<div class="text-danger push-right">
									{{ errors[0] }}
								</div>
							</validation-provider>
						</div>
						<div class="form-group">
							<label for="phone">Phone</label>
							<validation-provider
								rules="required|mobile_limit:10"
								v-slot="{ errors }"
							>
								<input
									type="text"
									id="phone"
									v-model="localUser.phone"
									:disabled="isDisabled"
									placeholder="Enter your phone number"
								/>
								<div class="text-danger push-right">
									{{ errors[0] }}
								</div>
							</validation-provider>
						</div>
						<div class="form-group">
							<label for="email">Email</label>
							<validation-provider rules="required|email" v-slot="{ errors }">
								<input
									type="email"
									id="email"
									v-model="localUser.email"
									:disabled="isDisabled"
									placeholder="Enter your email"
								/>
								<div class="text-danger push-right">
									{{ errors[0] }}
								</div>
							</validation-provider>
						</div>
						<div class="form-group">
							<label for="password">Password</label>
							<validation-provider
								rules="required|min:6|max:30"
								v-slot="{ errors }"
								vid="confirm_password"
							>
								<input
									name="password"
									type="password"
									id="password"
									v-model="localUser.password"
									:disabled="isDisabled"
									placeholder="Enter your password"
								/>
								<div class="text-danger push-right">
									{{ errors[0] }}
								</div>
							</validation-provider>
						</div>
						<div class="form-group">
							<label for="address" class="textarea-label">Address</label>
							<validation-provider
								rules="required|min:3|max:255"
								v-slot="{ errors }"
							>
								<textarea
									type="text"
									id="address"
									v-model="localUser.address"
									:disabled="isDisabled"
									placeholder="Enter your address"
								></textarea>
								<div class="text-danger push-right">
									{{ errors[0] }}
								</div>
							</validation-provider>
						</div>
						<div>
							<button
								v-if="isDisabled === true"
								class="btn-bg btn-yellow push-right"
								@click.prevent="isDisabled = false"
							>
								Update profile
							</button>
							<b-button
								v-else
								@click="show = true"
								class="btn-bg btn-yellow push-right"
								:disabled="invalid"
								>Save Profile</b-button
							>
						</div>

						<b-modal
							v-model="show"
							id="profile-confirm"
							title="Confirm profile save"
						>
							<p class="my-4">Are your sure you want to save your profile?</p>
							<template #modal-footer>
								<b-button
									size="md"
									class="float-right btn-red"
									@click="resetProfile()"
								>
									Reset
								</b-button>
								<b-button
									size="md"
									class="float-right btn-yellow"
									@click="saveProfile()"
								>
									Save Profile
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
import { mapActions, mapGetters } from 'vuex';
import { ValidationProvider, ValidationObserver } from 'vee-validate';

export default {
	name: 'Profile',
	data() {
		return {
			localUser: {
				name: '',
				phone: '',
				email: '',
				password: '',
				confirm_password: '',
				address: '',
			},
			// dummyUser is used to check if the user has changed any of the fields
			// it is the first copy of the user data on mounting the component
			dummyUser: {},
			isDisabled: true,
			show: false,
		};
	},
	components: {
		ValidationObserver,
		ValidationProvider,
	},
	computed: {
		...mapGetters(['getUser']),
	},
	beforeMount() {
		this.localUser = this.getUser;
	},
	mounted() {
		this.dummyUser = {
			access_token: this.localUser.access_token,
			name: this.localUser.name,
			address: this.localUser.address,
			email: this.localUser.email,
			phone: this.localUser.phone,
			password: this.localUser.password,
		};
	},
	methods: {
		...mapActions(['updateProfile']),
		resetProfile() {
			this.localUser = this.dummyUser;
			this.isDisabled = true;
			this.show = false;
		},
		checkUpdate() {
			if (
				this.localUser.name !== this.dummyUser.name ||
				this.localUser.address !== this.dummyUser.address ||
				this.localUser.email !== this.dummyUser.email ||
				this.localUser.phone !== this.dummyUser.phone ||
				this.localUser.password !== this.dummyUser.password
			) {
				return true;
			}
			return false;
		},
		saveProfile() {
			this.isDisabled = true;
			if (this.checkUpdate()) {
				this.updateProfile({
					cust_id: this.localUser.cust_id,
					name: this.localUser.name,
					email: this.localUser.email,
					phone: this.localUser.phone,
					password: this.localUser.password,
					address: this.localUser.address,
				})
					.then(() => {
						this.dummyUser = this.localUser;
						alert('Your profile has been succesfully updated!');
					})
					.catch(() => {
						alert('An error has occurred!');
					});
			}
			this.show = false;
		},
	},
};
</script>

<style scoped>
.profile {
	display: flex;
	justify-content: center;
	align-items: center;
	margin: 50px 0 100px 0;
}
.profile-form {
	background-color: #f5f5f5;
	padding: 50px 200px;
}
.profile-form-header {
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
.btn-bg {
	width: 140px;
	padding: 6px 10px;
	margin-top: 20px;
	display: flex;
	align-items: center;
	justify-content: center;
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
