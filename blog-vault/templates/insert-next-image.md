<%*
const prefix = await tp.system.prompt(
    "Image Filename Prefix"
);

if (!prefix || !prefix.trim()) {
    return;
}


const start = await tp.system.prompt(
    "Starting Number"
);

if (!start || !start.trim()) {
    return;
}


const end = await tp.system.prompt(
    "Ending Number"
);

if (!end || !end.trim()) {
    return;
}

const startNumber = Number(start);
const endNumber = Number(end);

// Validate numbers
if (
    !Number.isInteger(startNumber) ||
    !Number.isInteger(endNumber) ||
    startNumber > endNumber
) {
    return;
}

// Generate image tags
let output = "";

for (let i = startNumber; i <= endNumber; i++) {
    output += `![[${prefix}${i}.png|640]]\n\n`;
}

tR += output;
%>