def get_repo_info(username_tag,star_tag):
  a_tag = username_tag.find_all('a')
  name = a_tag[0].text.strip()
  ur = a_tag[1].text.strip()
  repo = base_url + a_tag[1]['href']
  st = stars_count(star_tag.text)
  return name,ur,repo,st
  topic_dict = {
    'username':[],
    'repo_name':[],
    'repo_url':[],
    'star':[]
}
for i in range(len(username)):
  repo_info = get_repo_info(username[i],repo_stars[i])
  topic_dict['username'].append(repo_info[0])
  topic_dict['repo_name'].append(repo_info[1])
  topic_dict['repo_url'].append(repo_info[2])
  topic_dict['star'].append(repo_info[3])

topic_dict = {
    'username':[],
    'repo_name':[],
    'repo_url':[],
    'star':[]
}
for i in range(len(username)):
  repo_info = get_repo_info(username[i],repo_stars[i])
  topic_dict['username'].append(repo_info[0])
  topic_dict['repo_name'].append(repo_info[1])
  topic_dict['repo_url'].append(repo_info[2])
  topic_dict['star'].append(repo_info[3])
  def get_topic_url(topic_doc):

   ## get h3 tags
  username = doc2.find_all('h3',{'class':'f3 color-fg-muted text-normal lh-condensed'})

   ## stars
  repo_stars = doc2.find_all('span',{'id':'repo-stars-counter-star'})

  ## Topics Dictionary
  topic_dict = {
      'username':[],
      'repo_name':[],
      'repo_url':[],
      'star':[]
      }

   ## all repo info
  for i in range(len(username)):
    repo_info = get_repo_info(username[i],repo_stars[i])
    topic_dict['username'].append(repo_info[0])
    topic_dict['repo_name'].append(repo_info[1])
    topic_dict['repo_url'].append(repo_info[2])
    topic_dict['star'].append(repo_info[3])

   ## Now convert it into data frame
    return pd.DataFrame(topic_dict)
