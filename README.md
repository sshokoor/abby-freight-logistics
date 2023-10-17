# Local Business Website Setup and Documentation with Jinja2

## Table of Contents

- [Bootstrap Styling](#bootstrap-styling)
- [Schema.org Structuring](#schema-structure)
- [Domain Registration](#domain-registration)
- [Google Business Integration](#google-business-integration)
- [Website Analytics](#website-analytics)

## Bootstrap 
[Bootsrap Template](https://getbootstrap.com/docs/5.3/examples/album/) used for the template/formatting of the website 

## Schema.org Structuring

To indicate that your website is for a local business, you can use Schema.org structured data (JSON-LD). Here's an example of how to incorporate it into your HTML:
 
```<script type="application/ld+json">
    {
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    "address": {
        "@type": "PostalAddress",
        "addressLocality": "insert_city",
        "addressRegion": "insert_state",
        "postalCode": "insert_zip",
        "streetAddress": "insert_address"
    },
    "name": "{{ company_name }}",
    "openingHours": [
        "Mo-Su 8:00-16:00"
    ],
    "areaServed": {
        "@type": "Place",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Tracy",
            "addressRegion": "CA"
        },
    "telephone": "{{ company_number }}",
    "url": "TBA"
    }
    }
```
## Domain Registration

Setting up a custom domain is the first step in establishing an online presence for your business. Here's how to do it:

1. Choose a reliable domain registrar (e.g., GoDaddy, Namecheap, Google Domains).
2. Search for an available domain name that represents your business.
3. Register the domain and configure DNS settings.
4. Link the domain to your website hosting provider.

## Google Business Integration

Google Business is an essential tool for businesses to manage their online presence and enhance visibility in Google Search and Maps. Here's how to integrate it:

1. Create a Google Business account or claim an existing listing.
2. Verify your business to gain ownership.
3. Update your business information, including address, phone number, hours of operation, and website link.
4. Encourage customers to leave reviews and respond to them.
5. Regularly check and update your listing to keep it accurate.

## Website Analytics

Tracking website analytics is crucial for understanding user behavior and optimizing your website's performance. You can use Google Analytics for this purpose:

1. Sign up for a Google Analytics account.
2. Set up a property for your website and get the tracking code.
3. Insert the tracking code into the HTML of your website, just before the closing </body> tag.

## Authors

- [@sshokoor](https://www.github.com/sshokoor)
- [@skittleson](https://github.com/skittleson)

## Resources

- [Schema Structure](https://schema.org/LocalBusiness)
- [Python Template](https://zetcode.com/python/jinja/)

## Contact
If you have any questions or comments about my work, please open an issue on this repository or contact me by [my email](sarahshokoor@gmail.com).