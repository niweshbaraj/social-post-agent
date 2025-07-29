# LangSmith Integration Guide

This document explains how to set up and use LangSmith for observability and monitoring in the Social Post Agent project.

## What is LangSmith?

LangSmith is LangChain's observability platform that helps you:
- **Debug** your LangChain applications with detailed traces
- **Monitor** performance and usage in production
- **Evaluate** your models and chains
- **Optimize** your AI workflows

## Setup Instructions

### 1. Get LangSmith API Key

1. Visit [LangSmith](https://smith.langchain.com/)
2. Sign up or log in to your account
3. Navigate to **Settings** → **API Keys**
4. Create a new API key and copy it

### 2. Configure Environment Variables

Add the following to your `.env` file:

```bash
# LangSmith Configuration
LANGCHAIN_API_KEY=your_langchain_api_key_here
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=social-post-agent
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
```

### 3. Install Dependencies

LangSmith is already included in your `requirements.txt`:

```bash
pip install langsmith
```

## Features Integrated

### 1. Workflow Tracing

The main workflow endpoint (`/post_content/`) is now traced with LangSmith:
- Complete workflow execution tracking
- Input/output logging
- Performance metrics
- Error tracking

### 2. Individual Node Tracing

Each workflow node is individually traced:

- **`generate_post`**: Content generation with platform-specific prompts
- **`evaluate_post`**: Quality evaluation and compliance checking
- **`optimize_post`**: Content optimization based on feedback
- **`generate_ai_image`**: AI image generation
- **`text_post`**: Text posting to social platforms
- **`media_post`**: Media posting to social platforms

### 3. Platform-Specific Monitoring

Track performance across different platforms:
- Twitter/X posting success rates
- LinkedIn engagement optimization
- Instagram content compliance

## Using LangSmith Dashboard

### 1. View Traces

1. Go to [LangSmith Dashboard](https://smith.langchain.com/)
2. Select your project: **social-post-agent**
3. View real-time traces of your workflow executions

### 2. Debug Issues

- **Failed Posts**: See exactly where posting failures occur
- **Content Quality**: Track evaluation scores and feedback
- **API Errors**: Monitor platform-specific API issues
- **Performance**: Identify slow components

### 3. Monitor Usage

- **Request Volume**: Track API usage patterns
- **Success Rates**: Monitor posting success across platforms
- **Cost Tracking**: Monitor AI model usage costs
- **User Patterns**: Understand how the agent is being used

## Example Trace Structure

When you run the Social Post Agent, you'll see traces like:

```
social_post_workflow
├── generate_post (Platform: twitter)
│   ├── Input: {"topic": "AI trends", "platform": "twitter"}
│   └── Output: {"post": "🤖 AI is transforming...", "title": "AI Trends"}
├── evaluate_post
│   ├── Input: {"post": "🤖 AI is transforming...", "platform": "twitter"}
│   └── Output: {"status": "approve", "feedback": "Great engagement potential"}
└── text_post
    ├── Input: {"post": "🤖 AI is transforming...", "platform": "twitter"}
    └── Output: {"status_code": 201, "response": {"id": "tweet_123"}}
```

## Advanced Configuration

### Custom Project Names

You can customize the project name by setting:

```bash
LANGCHAIN_PROJECT=my-custom-project-name
```

### Sampling

For high-volume usage, you can implement sampling:

```python
import random
from langsmith import traceable

@traceable(name="my_function", sample_rate=0.1)  # Trace 10% of requests
def my_function():
    pass
```

### Custom Metadata

Add custom metadata to traces:

```python
from langsmith import traceable

@traceable(name="generate_post", metadata={"platform": "twitter", "version": "1.0"})
def generate_post(state):
    # Your code here
    pass
```

## Troubleshooting

### Common Issues

1. **No Traces Appearing**
   - Check your API key is correct
   - Ensure `LANGCHAIN_TRACING_V2=true`
   - Verify network connectivity

2. **API Key Errors**
   - Regenerate your API key
   - Check for extra spaces in `.env` file
   - Ensure environment variables are loaded

3. **Project Not Found**
   - Projects are created automatically
   - Check the project name spelling
   - Refresh the LangSmith dashboard

### Debug Mode

Enable debug logging to troubleshoot:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Benefits for Social Post Agent

### 1. Content Quality Monitoring
- Track which topics generate better content
- Monitor evaluation scores over time
- Identify optimization patterns

### 2. Platform Performance
- Compare success rates across Twitter, LinkedIn, Instagram
- Monitor API response times
- Track posting failures and their causes

### 3. User Experience
- Identify slow workflow steps
- Monitor error rates
- Optimize based on usage patterns

### 4. Cost Optimization
- Track AI model usage
- Monitor expensive operations
- Optimize prompt efficiency

## Next Steps

1. **Set up your API key** and start seeing traces
2. **Explore the dashboard** to understand your workflow patterns
3. **Set up alerts** for failed posts or high error rates
4. **Use evaluation datasets** to improve content quality
5. **Monitor costs** and optimize model usage

For more advanced features, check the [LangSmith Documentation](https://docs.smith.langchain.com/).
