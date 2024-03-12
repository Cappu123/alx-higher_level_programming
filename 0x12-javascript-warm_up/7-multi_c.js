#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined)
{
	console.log('Missing number of occurrences');
}
else
{
	const occurrence = Number(process.argv[2]);
	let i = 0;
	while (i < occurrence)
	{
		console.log('C is fun');
		i++;
	}
}

