# -*- coding: utf-8 -*-
import scrapy


class MuglaPersonelInfSpider(scrapy.Spider):
    name = "mugla_personel_inf"
    allowed_domains = ["mu.edu.tr"]
    start_urls = ['http://www.personel.mu.edu.tr/tr/personel/idari']

    def parse(self, response):
        personnel_links = response.css(".bilgi span.detay a::attr('href')").extract()
        for link in personnel_links:
        	if link != "#":
        		yield scrapy.Request(link, callback=self.parse_personnel_inf)

    def parse_personnel_inf(self, response):
    	personnel_name = response.css(".cv_name #ContentPlaceHolder1_Personel1_lbl_name::text").extract_first()
    	personnel_mail = response.css("#ContentPlaceHolder1_Personel1_lbl_contact .col-md-9::text")[0].extract()
    	personnel_job = response.css(".cv_title #ContentPlaceHolder1_Personel1_lbl_title::text").extract()
    	yield{
    		'name' : personnel_name,
    		'email' : personnel_mail,
    		'job' : personnel_job

    	}
