# al-qaida-sanctions

## United Nations ISIL and Al-Qaida Sanctions D3 Force-Directed Graph Visualization

Deployed Website: https://al-qaida-sanctions.com/

This application uses the [D3 JavaScript library](https://d3js.org/) to render a force-directed graph showing the relationships between 
sanctioned individuals and entities from the public [United Nations Al-Qaida Sanctions List](https://www.un.org/securitycouncil/sanctions/1267). The [data](data/AQList.xml)
 is published by the United Nations and is publicly available on a U.N. website.

By hovering your mouse pointer over a graph node you can view a tooltip identifying the sanctioned individual or organization:

![Hover over a node](./images/nusrat.png)

Click on a graph node to see additional details regarding the sanction entity at the bottom of the screen:

![Click on a node](./images/al-qaida-sanctions-rouine.png)

Follow these steps to run this app on your local machine:

```shell
git clone https://github.com/johnfkraus/al-qaida-sanctions.git

cd al-qaida-sanctions

npm install

npm start
```
Browse to localhost:3000

## References

[United Nations Security Council Committee pursuant to resolutions 1267 (1999) 1989 (2011) and 2253 (2015) concerning Islamic State in Iraq and the Levant (Da’esh), Al-Qaida and associated individuals, groups, undertakings and entities](https://www.un.org/securitycouncil/sanctions/1267)

[United Nations Sanctions List Materials](
https://www.un.org/securitycouncil/sanctions/1267/aq_sanctions_list)

[United Nations Narrative Summaries of Reasons for Listing](https://www.un.org/securitycouncil/sanctions/1267/aq_sanctions_list/summaries?type=All&page=0&order=field_posted_on&sort=desc)

[Wikipedia: United Nations ISIL (Da'esh) and Al-Qaida Sanctions Committee](https://en.wikipedia.org/wiki/ISIL_(Da%27esh)_and_Al-Qaida_Sanctions_Committee)

