<template>
	<div class="register">
		<div class="register-form">
			<div class="register-form-header">Register your account!</div>
			<div class="register-form-body">
				<validation-observer v-slot="{ invalid, handleSubmit }">
					<form @submit.prevent="handleSubmit(register)">
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
									v-model="phone"
									placeholder="Enter your phone number"
								/>
								<div class="text-danger push-right">
									{{ errors[0] }}
								</div>
							</validation-provider>
						</div>
						<div class="form-group">
							<label for="name">Admin/User</label>
							<validation-provider
								rules="required|min:3|max:30"
								v-slot="{ errors }"
							>
								<select v-model="isAdmin">
									<option value="user" default>User</option>
									<option value="admin">Admin</option>
								</select>
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
									v-model="email"
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
									v-model="password"
									placeholder="Enter your password"
								/>
								<div class="text-danger push-right">
									{{ errors[0] }}
								</div>
							</validation-provider>
						</div>
						<div class="form-group">
							<label for="confirm_password">Confirm Password</label>
							<validation-provider
								rules="required|confirmed:confirm_password"
								v-slot="{ errors }"
							>
								<input
									type="password"
									id="confirm_password"
									v-model="confirm_password"
									placeholder="Re-enter your password"
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
									v-model="address"
									placeholder="Enter your address"
								></textarea>
								<div class="text-danger push-right">
									{{ errors[0] }}
								</div>
							</validation-provider>
						</div>
						<b-button
							@click="show = true"
							:disabled="invalid"
							class="btn btn-yellow push-right"
							>Register</b-button
						>

						<b-modal
							v-model="show"
							id="register"
							title="Confirm Account Creation"
						>
							<p class="my-4">Do you want to create an account?</p>
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
									@click="register()"
								>
									Register
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
import { mapActions } from 'vuex';
import { ValidationProvider, ValidationObserver } from 'vee-validate';

export default {
	name: 'Register',
	data() {
		return {
			name: '',
			email: '',
			phone: '',
			password: '',
			confirm_password: '',
			address: '',
			show: false,
			isAdmin: 'user'
		};
	},
	components: {
		ValidationObserver,
		ValidationProvider,
	},
	methods: {
		...mapActions(['registerUser']),
		register() {
			this.registerUser({
				name: this.name,
				email: this.email,
				phone: this.phone,
				password: this.password,
				address: this.address,
				isAdmin: this.isAdmin,
			})
				.then(() => {
					alert(
						'Your account has been sucessfully created! Please login to continue',
					);
					this.$router.push('/login');
				})
				.catch(() => {
					alert('Something went wrong!');
				});
			this.show = false;
		},
	},
};
</script>

<style scoped>
.register {
	display: flex;
	justify-content: center;
	align-items: center;
	margin: 50px 0 100px 0;
}
.register-form {
	background-color: #f5f5f5;
	padding: 50px 200px;
}
.register-form-header {
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
