import React, {useState, useEffect} from "react";
import jsYaml from "js-yaml";

export default function ComposeInstruction() {
	const [data, setData] = useState([]);

	useEffect(() => {
    fetch("http://127.0.0.1:8080/api/dockercompose/instruction/")
      .then((response) => response.text())
      .then((yamlData) => {
        const jsonData = jsYaml.load(yamlData)
        setData(jsonData);
      })
      .catch((error) => console.error("Error fetching data:", error));
  }, []);

	return (
		<div>
      <ul>
        {data.map(item => (
          <li key={item.id}>{item.key}: {item.value}</li>
        ))}
      </ul>
    </div>
	);
}
