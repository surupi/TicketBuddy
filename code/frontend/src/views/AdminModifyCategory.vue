<template>
	<div class="modify-category">
		<div class="modify-category-form">
			<div class="modify-category-form-header">
				Update the details of the category
			</div>
			<div class="modify-category-form-body">
				<validation-observer v-slot="{ invalid, handleSubmit }">
					<form @submit.prevent="handleSubmit(saveCategory)">
						<div class="form-group">
							<label for="name">Category Name</label>
							<validation-provider
								rules="required|min:3|max:30"
								v-slot="{ errors }"
							>
								<input
									type="text"
									id="name"
									v-model="localCategory.name"
									:disabled="isDisabled"
									placeholder="Enter the name of the category"
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
									v-model="localCategory.description"
									:disabled="isDisabled"
									placeholder="Enter the description of the category"
								></textarea>
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
								Update Category
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
							id="category-modify-confirm"
							title="Confirm Category Modification"
						>
							<p class="my-4">Are your sure you want to save this category?</p>
							<template #modal-footer>
								<b-button
									size="md"
									class="float-right btn-red"
									@click="resetCategory()"
								>
									Reset
								</b-button>
								<b-button
									size="md"
									class="float-right btn-yellow"
									@click="saveCategory()"
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
	name: 'ModifyCategory',
	data() {
		return {
			localCategory: {
				name: '',
				description: '',
			},
			dummyCategory: {}, // dummyCategory is used to check if the user has changed any of the fields
			isDisabled: true,
			show: false,
		};
	},
	components: {
		ValidationObserver,
		ValidationProvider,
	},
	computed: {
		...mapGetters(['getCategory', 'getAdminID', 'getAccessToken']),
	},
	async beforeMount() {
		this.localCategory = this.getCategory;
	},
	mounted() {
		this.dummyCategory = {
			category_id: this.localCategory.category_id,
			name: this.localCategory.name,
			description: this.localCategory.description,
		};
	},
	methods: {
		resetCategory() {
			this.localCategory = this.dummyCategory;
			this.isDisabled = true;
			this.show = false;
		},
		checkUpdate() {
			if (
				this.localCategory.category_id !== this.dummyCategory.category_id ||
				this.localCategory.name !== this.dummyCategory.name ||
				this.localCategory.description !== this.dummyCategory.description
			) {
				return true;
			}
			return false;
		},
		async saveCategory() {
			if (this.checkUpdate()) {
				const categoryData = {
					name: this.localCategory.name,
					description: this.localCategory.description,
				};
				await axios
					.put(
						`http://localhost:5000/modifycategory/${this.$route.params.category_id}`,
						categoryData,
						{
							headers: {
								'Content-Type': 'application/json',
								Authorization: `Bearer ${this.getAccessToken}`
							},
						},
					)
					.then(() => {
						alert('Category updated successfully');
					})
					.catch(() => {
						alert('Error updating category');
					});
			}
			this.show = false;
			this.isDisabled = true;
		},
	},
};
</script>

<style scoped>
.modify-category {
	display: flex;
	justify-content: center;
	align-items: center;
	margin: 50px 0 100px 0;
}
.modify-category-form {
	background-color: #f5f5f5;
	padding: 50px 200px;
}
.modify-category-form-header {
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
