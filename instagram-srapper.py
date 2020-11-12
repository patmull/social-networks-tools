<?php

function scrape_insta($username) {
	$insta_source = file_get_contents('http://instagram.com/'.$username);
	$shards = explode('window._sharedData = ', $insta_source);
	$insta_json = explode(';</script>', $shards[1]);
	$insta_array = json_decode($insta_json[0], TRUE);
	return $insta_array;
}

$my_account = 'institut_de_beaute_sothyspraha';

$results_array = scrape_insta($my_account);

// Pro další fotky stačí měnít index ['edges'][0]['node']
$latest_array_1 = $results_array['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges'][0]['node'];
$latest_array_2 = $results_array['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges'][1]['node'];
$latest_array_3 = $results_array['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges'][2]['node'];


echo '<h1>Poslední 3 foto z '.$my_account.':<h1/>';
echo '<a href="http://instagram.com/p/'.$latest_array_1['shortcode'].'"><img src="'.$latest_array_1['thumbnail_src'].'"></a></br>';
echo '<a href="http://instagram.com/p/'.$latest_array_2['shortcode'].'"><img src="'.$latest_array_2['thumbnail_src'].'"></a></br>';
echo '<a href="http://instagram.com/p/'.$latest_array_3['shortcode'].'"><img src="'.$latest_array_3['thumbnail_src'].'"></a></br>';
