<template>
	<div class="about">
		<div class="banner-container">
			<img class="banner" src="../assets/about-banner.png" alt="about-banner" />
			<div class="banner-text">
				<div class="heading">TicketBuddy</div>
				<div class="text">Ticket Managament System</div>
			</div>
		</div>

		<div class="about-us">
			<div class="container">
				<div class="section-heading">About Us</div>
				<p class="section-text">
					TicketBuddy is an online ticket management app that helps you get in touch with the latest movies.<br>
					Our aim is to provide seemless ticket booking experience to all our customers.<br>
					So what are you waiting for?<br>
					Secure your seats for the latest blockbusters, grab your popcorn, and immerse yourself in the magic of the big screen.<br>
					Get ready to embark on a journey of entertainment and excitement with TicketBuddy!<br>
				</p>
			</div>
		</div>

		<div class="outer-gallery">
			<div class="container" style="textalign: center">
				<div class="section-heading">Gallery</div>
				<div class="gallery">
					<img src="../assets/about-images/moviehall.jpg" alt="moviehall" />
					<img src="../assets/about-images/popcorn.jpg" alt="popcorn" />
					<img src="../assets/about-images/camera.jpg" alt="camera" />
					<img src="../assets/about-images/people.jpg" alt="people" />
					<img src="../assets/about-images/reel.jpg" alt="reel" />
				</div>
			</div>
		</div>
	</div>
</template>

<script></script>

<style scoped>
.banner-container {
	position: relative;
}

.banner {
	width: 100%;
}

.banner-text {
	text-align: center;
	position: absolute;
	top: 35%;
	left: 29%;
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

.about-us {
	padding: 80px 0;
	background-color: #f5f5f5;
	text-align: center;
}

.section-heading {
	font-size: 2.2rem;
	font-weight: bold;
	color: #000;
	padding-bottom: 40px;
	text-align: center;
}

.section-text {
	font-size: 1.1rem;
	color: #000;
}

.outer-gallery {
	padding: 60px 0 80px 0;
}

.gallery {
	display: flex;
	flex-wrap: wrap;
	justify-content: space-around;
}
.image {
	width: 280px;
	height: 300px;
	padding: 20px 40px;
	background-color: #fff;
	box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2);
	display: flex;
	justify-content: center;
	align-items: center;
	flex-direction: column;
}
</style>
