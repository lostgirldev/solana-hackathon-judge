
Project Name: ZoroX - Tiktok Memecoin Hunter


Project Description: An Autonomous AI Agent that browses TikTok to help you find the hottest memecoins before they pump


Project's X/Twitter: https://x.com/TokenHunterZoro


Project's Website: https://zorox-ai.vercel.app/


Project's GitHub: https://github.com/gabrielantonyxaviour/zorox






# ZoroX - Tiktok Memecoin Hunter Submission Analysis

## Overview
This hackathon submission, titled **ZoroX - Tiktok Memecoin Hunter**, is an autonomous AI agent designed to browse TikTok and identify trending memecoins before they experience significant price increases. The project leverages TikTok's trending data and integrates with Pump.fun's database to provide users with real-time analytics on memecoin performance. 

### Main Functionalities and Features
1. **Real-Time Hashtag Analysis**: Monitors TikTok for trending hashtags and classifies crypto-related content.
2. **Pattern Matching**: Matches trending TikTok memes with launched tokens to identify related coins.
3. **Data Insights**: Displays analytics such as trading volume and TikTok view counts for trending coins.
4. **Automated Social Media Updates**: Posts updates on Twitter about trending memecoins based on specific criteria.
5. **Monetization**: Offers a free version with limited access and a premium version for full access.

## Criteria Analysis

### 1. Correctness
**Score: 7/10**

**Strengths**: 
- The codebase appears to run without major errors, and the main functionalities are implemented as described in the README.

**Weaknesses**: 
- There are some commented-out sections and unused imports that could lead to confusion about the code's current state. For example, in `scraper/main.py`, there are several commented-out lines that suggest incomplete features or debugging attempts:
  ```python
  # while True:
  #     try:
  #         profile_index = int(input("\\nEnter the number of the profile where you\'re logged into TikTok: ")) - 1
  #         if 0 <= profile_index < len(profiles):
  #             selected_profile = profiles[profile_index]
  #             break
  #         else:
  #             print("Invalid selection. Please try again.")
  #     except ValueError:
  #         print("Please enter a valid number.")
  ```

**Improvements**: 
- Remove commented-out code or provide clear comments explaining why they are retained. This will enhance clarity and maintainability.

### 2. Readability
**Score: 6/10**

**Strengths**: 
- The code is generally structured well, with functions that have descriptive names, making it easier to understand their purpose.

**Weaknesses**: 
- Some functions are lengthy and could benefit from being broken down into smaller, more manageable pieces. For instance, the `process_search_term` function in `scraper/main.py` is quite long and handles multiple responsibilities:
  ```python
  while len(results) < max_results:
      # ... (code for processing videos)
  ```

**Improvements**: 
- Refactor long functions into smaller helper functions to improve readability. Additionally, consistent use of docstrings for all functions would enhance understanding.

### 3. Bugginess
**Score: 5/10**

**Strengths**: 
- The codebase does not exhibit critical bugs that prevent it from running.

**Weaknesses**: 
- There are several areas where error handling could be improved. For example, in the `process_search_term` function, the error handling is minimal, and exceptions are caught but not logged or handled appropriately:
  ```python
  except Exception as e:
      print(f"\\nError during scraping \'{keyword}\': {e}")
      break
  ```

**Improvements**: 
- Implement more robust error handling, including logging errors to a file or console for easier debugging. This will help in identifying issues during runtime.

### 4. Features
**Score: 8/10**

**Strengths**: 
- The submission includes a comprehensive set of features that align well with the hackathon's goals. The integration with TikTok and Pump.fun is a strong point.

**Weaknesses**: 
- Some features, such as the premium version and automated social media updates, are mentioned but not fully detailed in the codebase. For instance, the monetization logic is not clearly implemented in the provided code snippets.

**Improvements**: 
- Ensure that all features are fully implemented and tested. Providing more detailed documentation on how to access premium features would also be beneficial.

## Final Score
**Final Score: 6.5/10**

### Summary
The ZoroX submission demonstrates a solid understanding of the requirements and effectively implements key functionalities. However, there are areas for improvement in terms of code cleanliness, readability, and error handling. By addressing these weaknesses, the submission could significantly enhance its overall quality and maintainability.