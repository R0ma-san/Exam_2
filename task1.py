def country(**a):
    for i in a:
        print(a[i])
country(name='USA', population='330 million', is_democratic=True)
country(name='Kyrgyzstan', area='200 km2', 
	have_borders_with=['Kazakhstan', 'Uzbekistan', 'Tajikistan', 'China'])