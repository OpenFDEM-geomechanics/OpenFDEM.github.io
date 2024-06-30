const express = require('express');
const { exec } = require('child_process');

const app = express();
const PORT = process.env.PORT || 3000;

app.get('/downloads', (req, res) => {
    const owner = 'OpenFDEM-geomechanics';
    const repo = 'OpenFDEM.github.io';

    exec(`gh release view --repo ${owner}/${repo} --json assets`, (err, stdout, stderr) => {
        if (err) {
            console.error(`Error: ${stderr}`);
            return res.status(500).json({ error: 'Failed to fetch download statistics' });
        }

        try {
            const data = JSON.parse(stdout);
            let totalDownloads = 0;

            data.assets.forEach(asset => {
                totalDownloads += asset.download_count;
            });

            res.json({ totalDownloads });
        } catch (error) {
            console.error(`Parsing error: ${error}`);
            res.status(500).json({ error: 'Failed to parse download statistics' });
        }
    });
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
