<?php
// Connect to DB
$db_path = '/home/pi/Projects/hadrian/web/metrics.sqlite';
try {
    $db = new PDO("sqlite:$db_path");
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    echo "Connection failed: " . $e->getMessage();
    exit;
}

// Fetch all metrics 
$metrics = [];
$total_iterations = 0;
try {
    $stmt = $db->query('SELECT * FROM metrics');
    $metrics = $stmt->fetchAll(PDO::FETCH_ASSOC);

    foreach ($metrics as $metric) {
        $total_iterations += 1; 
    }
} catch (Exception $e) {
    echo "Error fetching metrics: " . $e->getMessage();
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hadrian Metrics</title>
    <style>
        body {
            background-color: #f4f7fa;
            font-family: 'Arial', sans-serif;
            color: #333;
            margin: 0;
            padding: 20px;
        }
        h1 {
            text-align: center;
            color: #4a90e2;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        th, td {
            padding: 12px;
            text-align: left;
        }
        th {
            background-color: #4a90e2;
            color: #fff;
        }
        tr:nth-child(even) {
            background-color: #e9f3fc;
        }
        tr:hover {
            background-color: #d3e4f5;
        }
        h2 {
            text-align: center;
            margin-top: 20px;
            color: #333;
        }
        .iteration-count {
            background-color: #4a90e2;
            color: #fff;
            padding: 10px;
            border-radius: 5px;
            display: inline-block;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
        }
        img {
            max-width: 150px; 
            height: auto; 
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Hadrian Metrics</h1>
        <table border="1">
            <tr>
                <th>What The Camera Saw</th> 
                <th>Action</th>
                <th>Timestamp</th>
            </tr>
            <?php foreach ($metrics as $metric): ?>
                <tr>
                    <td>
                        <img src="data:image/jpeg;base64,<?php echo base64_encode($metric['image']); ?>" alt="Iteration Image">
                    </td>
                    <td><?php echo htmlspecialchars($metric['action']); ?></td>
                    <td><?php echo htmlspecialchars($metric['timestamp']); ?></td>
                </tr>
            <?php endforeach; ?>
        </table>

        <h2>Total Iterations: <span class="iteration-count"><?php echo $total_iterations; ?></span></h2>
    </div>
</body>
</html>
