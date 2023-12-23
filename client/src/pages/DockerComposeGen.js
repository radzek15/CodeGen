import React from "react";

import ComposeInstruction from "../components/DockerComponents/ComposeInstruction";
import NavBar from "../components/NavBar/NavBar"

export default function DockerComposeGen() {
	return (
		<div>
			<NavBar />
			<h1>Compose instructions:</h1>
			<ComposeInstruction />
		</div>
	);
}
