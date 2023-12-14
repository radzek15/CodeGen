import React, {useState, useEffect} from "react";

export default function TestComponent() {
	const [data, setData] = useState([]);

	useEffect(() => {
		fetch("http://localhost:8080/api/nginx/conf/")
			.then(response => response.json())
			.then(data => setData(data))
			.catch(error => console.error('Error fetching data:', error));
	}, []);

	return (
		<div>
      <h1>Data from Django API:</h1>
      <ul>
        {data.map(item => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
    </div>
	);
}
