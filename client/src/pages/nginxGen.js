import React from "react";

import NginxInstruction from "../components/NginxComponents/nginxInstruction";
import NginxConf from "../components/NginxComponents/nginxConf";
import NavBar from "../components/NavBar/NavBar"

export default function NginxGen() {
	return (
		<div>
			<NavBar />
			<h1>Instructions</h1>
			<NginxInstruction />
			<h1>Configuration</h1>
			<NginxConf />
		</div>
	)
}
