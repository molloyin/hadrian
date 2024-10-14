<?php
$db_path = '/home/pi64/code/hadrian/web/metrics.sqlite';

if (isset($_POST['start_script'])) {
    exec('python3 -m hadrian > /dev/null 2>&1 &');
}

// Connect to DB
try {
    $db = new PDO("sqlite:$db_path");
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    echo "Connection failed: " . $e->getMessage();
    exit;
}

// Fetch all metrics from the database
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
<html>
<head>
    <title>Self-Driving RC Metrics</title>
</head>
<body>
    <h1>Self-Driving RC Metrics</h1>

    <form method="post">
        <button type="submit" name="start_script">Start Python Script</button>
    </form>

    <h2>Metrics:</h2>
    <table border="1">
        <tr>
            <th>Iteration</th>
            <th>Action</th>
            <th>Timestamp</th>
        </tr>
        <?php foreach ($metrics as $metric): ?>
            <tr>
                <td><?php echo htmlspecialchars($metric['iteration']); ?></td>
                <td><?php echo htmlspecialchars($metric['action']); ?></td>
                <td><?php echo htmlspecialchars($metric['timestamp']); ?></td>
            </tr>
        <?php endforeach; ?>
    </table>

    <h2>Total Iterations: <?php echo $total_iterations; ?></h2>
</body>
</html>
