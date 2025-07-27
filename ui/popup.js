const backendBaseUrl = 'http://localhost:8000'; // Change for deployment

const topicInput = document.getElementById('topic');
const maxIterInput = document.getElementById('max-iteration');
const genImgInput = document.getElementById('generate-image');
const twitterBtn = document.getElementById('twitter-btn');
const linkedinBtn = document.getElementById('linkedin-btn');
const instagramBtn = document.getElementById('instagram-btn');
const contentPre = document.getElementById('content');
const statusDiv = document.getElementById('status');

// Unified function to post content to any platform
async function postToSocialMedia(platform) {
  const topic = topicInput.value.trim();
  const maxIterations = parseInt(maxIterInput.value, 10) || 3;
  const generateImage = genImgInput.checked;

  if(!topic) {
    statusDiv.textContent = "Please enter a topic.";
    statusDiv.style.color = "#e74c3c";
    return;
  }

  // Clear previous output/status
  contentPre.textContent = '';
  statusDiv.textContent = `Generating post for ${platform}...`;
  statusDiv.style.color = "#3498db";

  try {
    const requestData = {
      topic: topic,
      max_iteration: maxIterations,
      generate_image: generateImage,
      platform: platform
    };

    const response = await fetch(`${backendBaseUrl}/post_content/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(requestData)
    });

    const result = await response.json();

    if (response.ok && result.data) {
      // Show generated post
      contentPre.textContent = result.data.post || '[No content generated]';
      
      if (result.data.status_code === 201) {
        statusDiv.innerHTML = `✅ Successfully posted to ${platform.charAt(0).toUpperCase() + platform.slice(1)}!`;
        statusDiv.style.color = "#27ae60";
        
        // Show additional info if available
        if (result.data.tweet_id) {
          statusDiv.innerHTML += ` (ID: ${result.data.tweet_id})`;
        }
      } else {
        statusDiv.innerHTML = `❌ Failed to post to ${platform}: ${result.message || 'Unknown error'}`;
        statusDiv.style.color = "#e74c3c";
      }
    } else {
      statusDiv.innerHTML = `❌ Error: ${result.message || 'Failed to generate post'}`;
      statusDiv.style.color = "#e74c3c";
    }
  } catch (err) {
    statusDiv.textContent = "❌ Error: " + (err.message || err.toString());
    statusDiv.style.color = "#e74c3c";
    console.error('Error posting to social media:', err);
  }
}

// Event listeners for each platform
twitterBtn.onclick = () => postToSocialMedia('twitter');
linkedinBtn.onclick = () => postToSocialMedia('linkedin');
instagramBtn.onclick = () => postToSocialMedia('instagram');
