<template>
	<div class="category">
		<div class="container">
			<div class="heading">Categories/Genres</div>
			<button class="btn btn-yellow" style="marginbottom: 20px">
				<router-link class="rlink" to="/adminaddcategory">
					+ Add Category
				</router-link>
			</button>
			<b-table class="border-top" striped :items="items" :fields="fields">
				<template #cell(update)="row">
					<b-button
						class="button btn btn-yellow"
						size="sm"
						@click="routeUpdateCategory(row.item)"
					>
						Modify
					</b-button>
				</template>
				<template #cell(delete)="row">
					<b-button
						class="btn btn-red"
						size="sm"
						@click="showDeletionModal(row.item.category_id)"
					>
						Delete
					</b-button>
				</template>
			</b-table>
			<b-modal
				v-model="show"
				id="delete-category"
				title="Confirm category deletion"
			>
				<p class="my-4">Are your sure you want to delete this category?</p>
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
						@click="deleteCategory()"
					>
						Delete Category
					</b-button>
				</template>
			</b-modal>
		</div>
	</div>
</template>

<script>
import axios from 'axios';
import { mapActions, mapGetters } from 'vuex';

export default {
	name: 'Category',
	data() {
		return {
			fields: [
				{
					key: 'category_id',
					label: 'Category ID',
					class: 'text-center',
				},
				{
					key: 'name',
					label: 'Category Name',
				},
				{
					key: 'description',
					label: 'Description',
					thStyle: 'width: 20%',
				},
				"update","delete"
			],
			items: [],
			show: false,
			selectedCategory: '',
		};
	},
	methods: {
		...mapActions(['loadCategories', 'routeModifyCategory']),
		...mapGetters(['getCategories', 'getAccessToken']),
		showDeletionModal(category_id) {
			this.show = true;
			this.selectedCategory = category_id;
			console.log(this.selectedCategory);
		},
		routeUpdateCategory(categoryData) {
			this.routeModifyCategory(categoryData);
			this.$router.push(`/adminmodifycategory/${categoryData.category_id}`);
		},
		async deleteCategory() {
			await axios
				.delete(`http://localhost:5000/deletecategory/${this.selectedCategory}`,{
					headers: {
						'Content-Type': 'application/json',
						Authorization: `Bearer ${this.getAccessToken()}`,
					},
				})
				.then(() => {
					alert('Category deleted successfully!');
				})
				.catch(() => {
					alert('Error deleting category!');
				});
			this.show = false;
			await this.reloadCategories();
		},
		async reloadCategories() {
			await this.loadCategories();
			this.items = await this.getCategories();
		},
	},
	async mounted() {
		await this.reloadCategories();
	},
};
</script>

<style scoped>
.category {
	padding: 100px 0;
}
.heading {
	font-size: 30px;
	font-weight: 600;
	margin-bottom: 20px;
}
.button {
	margin-right: 10px;
}
.btn-yellow {
	background-color: #e4c314 !important;
	color: #000 !important;
	font-weight: 600;
}
.btn-red {
	background-color: #ff918d;
	color: #000;
	font-weight: 600;
}
.rlink {
	color: #000;
	text-decoration: none;
}
</style>
