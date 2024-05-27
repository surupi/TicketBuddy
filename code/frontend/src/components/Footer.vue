<template>
	<div class="footer">
		<div class="container inner-footer">
			<div class="upper-container">
				<div class="left-container">
					<div class="heading">TicketBuddy</div>
					<div class="text">
						Your one stop solution for ticket booking. <br>
						Thank you for choosing TicketBuddy!<br>
						IIT Madras | Modern Application Development 2 Project 
					</div>
				</div>
				<div class="right-container">
					<div class="heading">Contact Us</div>
					<a href="https://instagram.com">
						<img class="social" src="../assets/ig.png" />
					</a>
					<a href="https://twitter.com">
						<img class="social" src="../assets/tw.png" />
					</a>
					<a href="https://facebook.com">
						<img class="social" src="../assets/fb.png" />
					</a>
				</div>
			</div>
			<div class="lower-container" >TicketBuddy | All Rights Reserved</div>
		</div>
	</div>
</template>

<script></script>

<style scoped>
@media only screen and (max-width: 1268px) {
	.upper-container {
		display: block !important;
	}
	.left-container,
	.right-container {
		width: 200px !important;
		padding: 1em 0 !important;
	}
	.lower-container {
		padding-bottom: 100px;
	}
	.text {
		width: 200px;
	}
}
.footer {
	width: 100%;
	min-height: 29vh;
	background-color: #000;
	color: #fff;
	padding-top: 3em;
}
.inner-footer {
	display: flex;
	flex-direction: column;
	align-items: center;
}
.upper-container {
	display: flex;
}
.heading {
	font-size: 24px;
	font-weight: 600;
	padding-bottom: 10px;
}
.left-container,
.right-container {
	width: 600px;
}
.left-container {
	padding-right: 100px;
}
.right-container {
	padding-left: 100px;
}
.text {
	width: 400px;
}
.lower-container {
	padding-top: 60px;
}
.social {
	padding-right: 8px;
}
</style>