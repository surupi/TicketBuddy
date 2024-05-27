<template>
	<div class="add-category">
		<div class="category">
			<div class="category-form">
				<div class="category-form-header">Add a category</div>
				<div class="category-form-body">
					<validation-observer v-slot="{ invalid, handleSubmit }">
						<form @submit.prevent="handleSubmit(submitCategory)">
							<div class="form-group">
								<label for="Category">Category</label>
								<validation-provider
									rules="required|min:3|max:20"
									v-slot="{ errors }"
								>
									<input
										type="text"
										id="state"
										v-model="name"
										placeholder="Enter the category name"
									/>
									<div class="text-danger push-right">
										{{ errors[0] }}
									</div>
								</validation-provider>
							</div>
							<div class="form-group">
								<label for="description" class="textarea-label"
									>Description</label
								>
								<validation-provider
									rules="required|min:3|max:255"
									v-slot="{ errors }"
								>
									<textarea
										type="text"
										id="description"
										v-model="description"
										placeholder="Enter the category description here"
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
								>Add Category</b-button
							>

							<b-modal
								v-model="show"
								id="add-category"
								title="Confirm category addition"
							>
								<p class="my-4">Are your sure you want to add this category?</p>
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
										@click="submitCategory(movie)"
									>
										Add Category
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
	name: 'AddCategories',
	data() {
		return {
			name: '',
			description: '',
			show: false,
		};
	},
	components: {
		ValidationObserver,
		ValidationProvider,
	},
	methods: {
		...mapActions(['loadCategories']),
		...mapGetters(['getVenue', 'getAccessToken']),
		async submitCategory() {
			const categoryData = {
				name: this.name,
				description: this.description,
			};
			await axios
				.post('http://localhost:5000/adminaddcategory', categoryData, {
					headers: {
						'Content-Type': 'application/json',
						Authorization: `Bearer ${this.getAccessToken()}`
					},
				})
				.then(() => {
					alert('Category added successfully!');
					this.$router.push(`/admincategories`);
				})
				.catch(() => {
					alert('Error adding category!');
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
.category {
	display: flex;
	justify-content: center;
	align-items: center;
	padding: 20px 0 40px 0;
	background-color: #f5f5f5;
}
.category-form {
	padding: 50px 200px;
}
.category-form-header {
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
