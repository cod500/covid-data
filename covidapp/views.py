from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "c19e1abc08msh01b00df75cf65d2p18f65cjsn1abe0d9eb309",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers).json()

# Create your views here.


def helloworldview(request):
    num_results = int(response['results'])
    covid_list = []

    for x in range(0, num_results):
        covid_list.append(response['response'][x]['country'])
        covid_list.sort()

    if request.method == "POST":
        selected_country = request.POST['selectedcountry']

        for x in range(0, num_results):
            if selected_country == response['response'][x]['country']:
                print(selected_country)

                if response['response'][x]['cases']['new'] == None:
                    new = response['response'][x]['cases']['new']
                else:
                    new_temp = int(response['response'][x]['cases']['new'])
                    new = '{:,}'.format(new_temp)

                if response['response'][x]['cases']['active'] == None:
                    active = response['response'][x]['cases']['active']
                else:
                    active_temp = int(
                        response['response'][x]['cases']['active'])
                    active = '{:,}'.format(active_temp)

                if response['response'][x]['cases']['critical'] == None:
                    critical = response['response'][x]['cases']['critical']
                else:
                    critical_temp = int(
                        response['response'][x]['cases']['critical'])
                    critical = '{:,}'.format(critical_temp)

                if response['response'][x]['cases']['recovered'] == None:
                    recovered = response['response'][x]['cases']['recovered']
                else:
                    recovered_temp = int(
                        response['response'][x]['cases']['recovered'])
                    recovered = '{:,}'.format(recovered_temp)

                total_temp = int(response['response'][x]['cases']['total'])
                total = '{:,}'.format(total_temp)

                deaths_temp = int(total_temp) - \
                    int(active_temp) - int(recovered_temp)
                deaths = '{:,}'.format(deaths_temp)

        context = {'selected_country': selected_country, 'new': new, 'active': active, 'critical': critical,
                   'recovered': recovered, 'total': total, 'deaths': deaths, 'countries': covid_list}
        return render(request, 'helloworld.html', context)

    context = {'countries': covid_list}
    return render(request, 'helloworld.html', context)
