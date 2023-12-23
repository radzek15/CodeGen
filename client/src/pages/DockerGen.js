import React from "react";

import DockerCommand from "../components/DockerComponents/DockerCommand";
import NavBar from "../components/NavBar/NavBar"

export default function DockerGen() {
	return (
		<div>
			<NavBar />
			<h1>Commands for docker:</h1>
			<DockerCommand />
		</div>
	);
}
