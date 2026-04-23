<?php
header('Content-Type: text/plain; charset=utf-8');

$secret_key = "hurda_merkezi_99";
$json_file = __DIR__ . "/fiyatlar.json";

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    if (!isset($_POST["key"]) || $_POST["key"] !== $secret_key) {
        http_response_code(403);
        exit("HATALI_KEY");
    }

    if (!isset($_POST["data"]) || empty($_POST["data"])) {
        http_response_code(400);
        exit("DATA_YOK");
    }

    $raw = $_POST["data"];
    $decoded = json_decode($raw, true);

    if (json_last_error() !== JSON_ERROR_NONE || !is_array($decoded)) {
        http_response_code(400);
        exit("GECERSIZ_JSON");
    }

    $clean_data = [];

    foreach ($decoded as $category) {
        if (!is_array($category)) {
            continue;
        }

        $title = isset($category["t"]) ? trim((string)$category["t"]) : "";
        $items = isset($category["i"]) && is_array($category["i"]) ? $category["i"] : [];

        if ($title === "") {
            continue;
        }

        $clean_items = [];

        foreach ($items as $item) {
            if (!is_array($item)) {
                continue;
            }

            $name = isset($item["n"]) ? trim((string)$item["n"]) : "";
            $price = isset($item["p"]) ? (float)$item["p"] : 0;

            if ($name === "" || $price <= 0) {
                continue;
            }

            $clean_items[] = [
                "n" => $name,
                "p" => round($price, 2),
                "change" => isset($item["change"]) ? $item["change"] : "same",
                "percent" => isset($item["percent"]) ? (float)$item["percent"] : 0
            ];
        }

        if (!empty($clean_items)) {
            $clean_data[] = [
                "t" => $title,
                "i" => $clean_items
            ];
        }
    }

    if (empty($clean_data)) {
        http_response_code(400);
        exit("VERI_BOS");
    }

    $payload = [
        "updated_at" => date("Y-m-d H:i:s"),
        "data" => $clean_data
    ];

    $json_text = json_encode($payload, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);

    if ($json_text === false) {
        http_response_code(500);
        exit("JSON_OLUSTURULAMADI");
    }

    if (file_put_contents($json_file, $json_text, LOCK_EX) === false) {
        http_response_code(500);
        exit("DOSYA_YAZILAMADI");
    }

    exit("OK");
}

if ($_SERVER["REQUEST_METHOD"] === "GET") {
    header('Content-Type: application/json; charset=utf-8');

    if (!file_exists($json_file)) {
        echo json_encode([
            "updated_at" => null,
            "data" => []
        ], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
        exit;
    }

    readfile($json_file);
    exit;
}

http_response_code(405);
echo "METHOD_NOT_ALLOWED";
?>