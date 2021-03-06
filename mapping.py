city_id_dict = {'Asheville': 0, 'Austin': 1, 'Boston': 2, 'Broward County': 3, 'Cambridge': 4,
                'Chicago': 5, 'Clark County': 6, 'Columbus': 7, 'Denver': 8, 'Jersey City': 9,
                'Los Angeles': 10, 'Nashville': 11, 'New Orleans': 12, 'New York City': 13,
                'Oakland': 14, 'Pacific Grove': 15, 'Portland': 16, 'Rhode Island': 17, 'Salem': 18,
                'San Diego': 19, 'San Francisco': 20, 'San Mateo County': 21,
                'San Clara Country': 22, 'Santa Cruz County': 23, 'Seattle': 24,
                'Twin Cities MSA': 25, 'Washington D.C.': 26}

id_city_dict = {0: 'Asheville', 1: 'Austin', 2: 'Boston', 3: 'Broward County', 4: 'Cambridge',
                5: 'Chicago', 6: 'Clark County', 7: 'Columbus', 8: 'Denver', 9: 'Jersey City',
                10: 'Los Angeles', 11: 'Nashville', 12: 'New Orleans', 13: 'New York City',
                14: 'Oakland', 15: 'Pacific Grove', 16: 'Portland', 17: 'Rhode Island', 18: 'Salem',
                19: 'San Diego', 20: 'San Francisco', 21: 'San Mateo County', 22: 'San Clara Country',
                23: 'Santa Cruz County', 24: 'Seattle',
                25: 'Twin Cities MSA', 26: 'Washington D.C.'}

hood_latlong_dict = {10: [746, 34.04046, -118.26244], 12: [231, 29.93557, -90.06926]}

id_pop_dict = {0: 'New Listing', 1: 'Low', 2: 'Average', 3: 'High', 4: 'Extremely Popular'}
pop_id_dict = {'New Listing': 0, 'Low': 1, 'Average': 2, 'High': 3, 'Extremely Popular': 4}

room_type_id_dict = {'Shared Room': 0, 'Private Room': 1, 'Entire Home': 2, 'Hotel Room': 3}
id_room_type_dict = {0: 'Shared Room', 1: 'Private Room', 2: 'Entire Home', 3: 'Hotel Room'}

city_latlong_dict = {0.0: [35.57874453940702, -82.55658508002875],
                     1.0: [30.283220299244316, -97.75300299176298],
                     2.0: [42.33751953150349, -71.08297803906524],
                     3.0: [26.100730532353005, -80.15030725174958],
                     4.0: [42.37262656948493, -71.10889725947523],
                     5.0: [41.89904946884507, -87.66404224511494],
                     6.0: [36.115950431555426, -115.1553760800795],
                     7.0: [39.98893217819731, -82.99525612825397],
                     8.0: [39.74085208778584, -104.97419012635699],
                     9.0: [40.72694050241162, -74.05479675643095],
                     10.0: [34.04613022869341, -118.31592329064955],
                     11.0: [36.161298064831485, -86.76949305750145],
                     12.0: [29.95840226825378, -90.0748187240168],
                     13.0: [40.729633214975856, -73.95074746253856],
                     14.0: [37.8118978308365, -122.23998523720358],
                     15.0: [36.621463016759776, -121.92083078212298],
                     16.0: [45.52818764540984, -122.65179200186857],
                     17.0: [41.56768859734551, -71.41139883969366],
                     18.0: [44.92734410153466, -123.03917499306928],
                     19.0: [32.77017793534333, -117.18311561189918],
                     20.0: [37.76716611693177, -122.42989077467759],
                     21.0: [37.56024389842393, -122.33386482662019],
                     22.0: [37.352147836694485, -121.96639046255807],
                     23.0: [36.98839068109479, -121.9780671737747],
                     24.0: [47.62583064067392, -122.33331940176427],
                     25.0: [44.972577104831544, -93.27391850699486],
                     26.0: [38.911354089688395, -77.01716847357274]}


nearby_id_link_dict = {0: ['https://i.pinimg.com/736x/a9/fd/2c/a9fd2ce738e7cac808942023c09e4499.jpg',
                           'https://assets.simpleviewinc.com/simpleview/image/upload/c_limit,h_1200,q_75,w_1200/v1/clients/asheville/history_20df72fc-b2c1-4a2a-bdea-f1f6f01bf5ce.jpg',
                           'https://d2n2b9suk51lyo.cloudfront.net/uploads/business_image/image/5983/medium_WNC_Nature_Center_1500399031-Screen_Shot_2017-07-18_at_1.23.49_PM.png'],
                       1: ['https://cdn.vox-cdn.com/thumbor/c4ZKzDrJEnsYTJJmu-Jz65QNsG4=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/16389492/Mount_Bonnell_shutterstock.jpg',
                           'https://i.pinimg.com/originals/67/ef/52/67ef52b62a97ab3d9ab4aaea6e1a7734.jpg',
                           'https://images.unsplash.com/flagged/photo-1568917052807-c674bd9009b0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1400&q=80'],
                       2: ['https://images.unsplash.com/flagged/photo-1568917052807-c674bd9009b0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1400&q=80',
                           'https://afar-production.imgix.net/uploads/images/post_images/images/H6SME2iDPZ/original_4bd330970c032d9223ecb01a28dd2170.jpg?1531776707?ixlib=rails-0.3.0&w=600&h=600&fit=crop&auto=format%2Ccompress&q=80',
                           'https://www.history.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTU3ODc4NjAyOTgwNzk2MTI3/hith-fenway-park-2.jpg'],
                       3: ['https://i.pinimg.com/originals/9b/a7/db/9ba7db18c0514b1c5b8b693cf2686a67.jpg',
                           'https://media-cdn.tripadvisor.com/media/photo-s/12/2b/f0/0b/photo1jpg.jpg',
                           'https://media-cdn.tripadvisor.com/media/photo-s/12/78/0b/3e/butterfly-world.jpg'],
                       4: ['https://anhistorianabouttown.com/wp-content/uploads/2019/03/Kings-College-Gate-interior-short-1024x1024.jpeg',
                           'https://assets.atlasobscura.com/media/W1siZiIsInVwbG9hZHMvcGxhY2VfaW1hZ2VzLzMxZDVlNTJmLTM5YjItNDM5Yy1hOWMzLTAxNjUzNWVmYzM3MTgyYTk5MDJkMzg0MjNmMjVmZV9RdWVlbnMnX0NvbGxlZ2VfLV9NYXRoZW1hdGljYWxfQnJpZGdlLmpwZyJdLFsicCIsInRodW1iIiwiNTgweDU4MCMiXSxbInAiLCJjb252ZXJ0IiwiLXF1YWxpdHkgODEgLWF1dG8tb3JpZW50Il1d/Queens%27_College_-_Mathematical_Bridge.jpg',
                           'https://statues.vanderkrogt.net/Foto/gb/gbee073.jpg'],
                       5: ['https://liveatone.com/wp-content/uploads/2019/07/ONE_LUXE_APARTMENTS_WHEELING_ART_INSTITUTE_CHICAGO.jpg',
                           'https://loopchicago.com/assets/Uploads/8bf36eae8a/blog_happy-12th-birthday-millennium-park-v2__FillWzEyMDAsMTIwMF0.jpg',
                           'https://d1marr3m5x4iac.cloudfront.net/images/edpborder500/I0-001/039/261/783-2.jpeg_/navy-pier-83.jpeg'],
                       6: ['https://www.tripsavvy.com/thmb/et-H_WI35W4Z1YqZPaq_yvS4PtA=/3377x3377/smart/filters:no_upscale()/Fountains-Bellagio-Las-Vegas-1-3af96de921564e0b8ea2dd1f233cdf7b.jpg',
                           'https://www.waldorfastorialasvegas.com/wp-content/uploads/2019/07/las-vegas-strip-840x840.jpg',
                           'https://cdn.britannica.com/58/156458-050-68649A2F/Hoover-Dam-border-Colorado-River-Arizona-Nevada.jpg'],
                       7: ['https://media-cdn.tripadvisor.com/media/photo-s/0e/ea/eb/de/columbus-zoo.jpg',
                           'https://www.fpconservatory.org/wp-content/uploads/2017/07/KJJ_9057-600x600.jpg',
                           'https://psmag.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTUzMjEzMTA5NjU2MzY0NjY0/gettyimages-605876756.jpg'],
                       8: ['https://img.grouponcdn.com/pwa_test/2RDoZnrXgxnsvkxqXVGcyhcFkXys/2R-669x446/v1/sc600x600.jpg',
                           'https://cdn.vox-cdn.com/thumbor/GwvqT9o8NnKEnaWL_69epdiBtT8=/0x0:2048x1536/1400x1400/filters:focal(828x420:1154x746):format(jpeg)/cdn.vox-cdn.com/uploads/chorus_image/image/52365515/8533619567_93262b4b95_k.0.jpeg',
                           'https://d.newsweek.com/en/full/1594773/colorado-state-capitol-building.jpg?w=1600&h=1600&q=88&f=15f7c8f1366fbf6d96759f99a83763f2'],
                       9: ['https://i.guim.co.uk/img/media/f222c156d2f2d0ee68327f0233e9ed631c9519ca/0_0_3645_2186/master/3645.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=efe0f2456091d7fd2f8d8c6044d116e2',
                            'https://www.langan.com/wp-content/uploads/2017/02/Liberty-Science-Center-600.jpg',
                            'https://img.travelawaits.com/quill/4/8/9/0/a/1/4890a13ad8e016a14be7d6676629093276517572.jpg'],
                       10: ['https://i.pinimg.com/originals/0b/1b/d2/0b1bd22875454b01bcc87bc40d7072f0.jpg',
                            'https://media.cntraveler.com/photos/5ee255bf0196b768320d94f4/1:1/w_2848,h_2848,c_limit/DisneylandCalifornia-D6DEXF.jpg',
                            'https://tmd.discoverlosangeles.com/sites/default/files/media/activities/points_of_interest/griffith-observatory-hollywood-sign-sunset.jpg'],
                       11: ['https://assets.podomatic.net/ts/f0/cf/3e/allensircy/3000x3000_14380129.jpg',
                            'https://images.theconversation.com/files/248943/original/file-20181205-186055-spp99r.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=1200&h=1200.0&fit=crop',
                            'https://www.fifthandb.com/wp-content/uploads/2020/02/5B-home-740x740-1.jpg'],
                       12: ['https://www.tripsavvy.com/thmb/_NtaX6kk61zl81DwiS2WHCw21AI=/2995x2995/smart/filters:no_upscale()/FrenchQuarter6-2607e9a35fb8479582c74e8e24893227.jpg',
                            'https://assets.simpleviewinc.com/simpleview/image/upload/c_fill,h_560,q_60,w_560/v1/clients/neworleans/NOTMC_33329_a48a1ee8-9e44-4bda-9824-d54fdb8097f1.jpg',
                            'https://bloximages.newyork1.vip.townnews.com/nola.com/content/tncms/assets/v3/editorial/a/20/a205af8a-d155-5c70-a6e0-18f69a3884dd/5dd72fa870112.image.jpg?crop=741%2C741%2C124%2C0&resize=1200%2C1200&order=crop%2Cresize'],
                       13: ['https://cdn.vox-cdn.com/thumbor/JMqrPS2RmaDK6S5zaMuIw03I5Ns=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/18971698/151006_19_00_22_5DSR9489.jpg',
                            'https://www.history.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTY1MTc1MTk3ODI0MDAxNjA5/topic-statue-of-liberty-gettyimages-960610006-promo.jpg',
                            'https://www.thechatwalny.com/wp-content/uploads/sites/17/2018/03/Chatwal-New-York-Local-Attractions-Central-Park-Aerial-View-1024x1024.jpg'],
                       14: ['https://i.pinimg.com/originals/25/68/43/256843d4c25c33293ebcb2338c015f23.jpg',
                            'https://cdn.vox-cdn.com/thumbor/-6QwzuG16TmoHAd0m1-YOiarrSo=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/19253007/5717773834_213aff2481_k.jpg',
                            'https://cdn.vox-cdn.com/thumbor/jqYlPggQ5lX3bmrSd81ZSqkavxI=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/19239289/12th_Street_Entrance.jpg'],
                       15: ['https://i.pinimg.com/originals/3a/c7/11/3ac7119ae3af18189b7c7a1bc02941cd.jpg',
                            'https://afar-production.imgix.net/uploads/images/post_images/images/7Casjl9ZqP/original_POI-0032_Point_Pinos_Lighthouse_Lisa_Corson-3789.jpg?1526438695?ixlib=rails-0.3.0&w=600&h=600&fit=crop&auto=format%2Ccompress&q=80',
                            'https://d3qvqlc701gzhm.cloudfront.net/thumbs/baa64daf27e9c7ed96f230c85217f0d4bc5010dc99c147bf9c425e511b907d15-375.jpg'],
                       16: ['https://3hm4vx15otpx2n5mp13bqbsk-wpengine.netdna-ssl.com/wp-content/uploads/2012/07/washington-playground-alameda.jpg',
                            'https://bloximages.newyork1.vip.townnews.com/yakimaherald.com/content/tncms/assets/v3/editorial/3/65/3650d6f6-d365-514c-944d-11fc08c00069/5da602b812ee6.image.jpg?crop=1237%2C1237%2C219%2C0&resize=1237%2C1237&order=crop%2Cresize',
                            'https://assets.atlasobscura.com/media/W1siZiIsInVwbG9hZHMvcGxhY2VfaW1hZ2VzL2U4MmFiOWVkNTI4NDA3MWQ4M18xMjAwcHgtUm9zZV9HYXJkZW4sX0p1bmVfMjAxNi5qcGciXSxbInAiLCJ0aHVtYiIsIjU4MHg1ODAjIl0sWyJwIiwiY29udmVydCIsIi1xdWFsaXR5IDgxIC1hdXRvLW9yaWVudCJdXQ/1200px-Rose_Garden%2C_June_2016.jpg'],
                       17: ['https://townsquare.media/site/518/files/2018/01/WaterFire-Providence.jpg',
                            'https://www.tripsavvy.com/thmb/9fFcgrH471aBDFhAieCofj8TIns=/2832x2832/smart/filters:no_upscale()/Newport-Cliff-Walk-5a86598e8e1b6e0036a87594.jpg',
                            'https://i.pinimg.com/originals/7b/47/25/7b4725810687e89ff460fc94ea2f9ba9.jpg'],
                       18: ['https://media.architecturaldigest.com/photos/5d1a2c7c8b62fb0009f89f9e/1:1/w_3011,h_3011,c_limit/PeabodyEssexMuseum%20photo%20by%20Aislinn%20Weidele_Ennead%20Architects_1.jpg',
                            'https://www.tripsavvy.com/thmb/e8xRVNJIFu0jOKAqeO0gJ6TCuuI=/1000x1000/smart/filters:no_upscale()/salemwitchmuseum-78e395a5a04b4ead89da4f215c9c7406.jpg',
                            'https://i.pinimg.com/originals/70/4e/d1/704ed19e7170ca660d8709f89603bfe7.png'],
                       19: ['https://i2.wp.com/www.hachettebookgroup.com/wp-content/uploads/2019/01/CA_SanDiego_BalboaPark_Dreamstime.jpg?resize=1080%2C1080&ssl=1',
                            'https://i.pinimg.com/originals/f8/d9/5d/f8d95d0b3099ad7838cdcdf263dc9c0c.jpg',
                            'https://geltechsolutions.com/fireice/wp-content/uploads/2018/07/San-Diego-Zoo-Challenge.jpg'],
                       20: ['https://www.history.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTY1MTc3MjE0MzExMDgxNTQ1/topic-golden-gate-bridge-gettyimages-177770941.jpg',
                            'https://img-aws.ehowcdn.com/560x560p/s3-us-west-1.amazonaws.com/contentlab.studiod/getty/8ca37fc971794b4eafdafb65d38159d7',
                            'https://img.static-kl.com/images/media/4FF03D3A-CA85-456A-8A96A1CF42192208?aspect_ratio=1:1&min_width=912'],
                       21: ['https://i.pinimg.com/originals/c4/09/4b/c4094b7335f6444d356eb239a5d01ae7.jpg',
                            'https://i.pinimg.com/originals/9a/d2/29/9ad2292669c3196de082d9a0412388c1.jpg',
                            'https://i.guim.co.uk/img/media/50f7a1efd00676dba5d799e46ccd22689112fad1/0_339_5056_3035/master/5056.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=1ff9a74fe6a877d22805b2a8c8e08edf'],
                       22: ['https://cdn.vox-cdn.com/thumbor/KlBHBhqZYo02fsvmGpdsWu282Q4=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/21923127/1175987442.jpg.jpg',
                            'https://media-cdn.tripadvisor.com/media/photo-s/14/41/0e/61/photo1jpg.jpg',
                            'https://www.scu.edu/media/offices/global-engagement/photos-for-buttons/cat-1/cat-8/LANDSCAPES_Yue-Hu_Denver.jpg'],
                       23: ['https://www.sanjose.org/sites/default/files/styles/listing_detail_image/public/2017-10/r_1.jpg?itok=rsqX2kzU',
                            'https://www.sanjose.org/sites/default/files/styles/listing_detail_image/public/2017-10/p_2.jpg?itok=a_uAa1_4',
                            'https://www.sanjose.org/sites/default/files/styles/listing_detail_image/public/2017-10/wsii-2102_0.jpg?itok=WYRN28qO'],
                       24: ['https://www.panpacificseattle.com/wp-content/uploads/2017/08/Chihuly-Garden-Glass-in-Seattle.jpg',
                            'https://cdn.vox-cdn.com/thumbor/ODal3bbEgzSe6w2LyJ0jWcMks70=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/10915759/PikePlaceMarket1.jpg',
                            'https://www.tripsavvy.com/thmb/9F-23TwLMR2vOC5OQkye71Xuuws=/1369x1369/smart/filters:no_upscale()/GettyImages-610712690-5c3ba9c646e0fb00018dead8.jpg'],
                       25: ['https://i.pinimg.com/736x/5a/7e/db/5a7edbfa4d398ddc5a73299df429058d.jpg',
                            'https://www.americanrivers.org/wp-content/uploads/2016/03/B-9-713x713.png',
                            'https://d1marr3m5x4iac.cloudfront.net/images/edpborder500/I0-001/004/400/621-0.jpeg_/walker-art-center-21.jpeg'],
                       26: ['https://washington-org.s3.amazonaws.com/s3fs-public/styles/gallery_full/public/trippingovertravel_winter-evening-columns-at-wwii-memorial_yesmydccool.jpg?itok=Q1ACVt5-',
                            'https://pbs.twimg.com/profile_images/1016670443560988672/bLMYqlx9.jpg',
                            'https://media.architecturaldigest.com/photos/56c7af26cd3bcb326e99b545/1:1/w_3075,h_3075,c_limit/lincoln-center-renovation-01.jpg']}


nearby_city_link_dict={'Asheville': ['https://i.pinimg.com/736x/a9/fd/2c/a9fd2ce738e7cac808942023c09e4499.jpg',
                            'https://assets.simpleviewinc.com/simpleview/image/upload/c_limit,h_1200,q_75,w_1200/v1/clients/asheville/history_20df72fc-b2c1-4a2a-bdea-f1f6f01bf5ce.jpg',
                            'https://d2n2b9suk51lyo.cloudfront.net/uploads/business_image/image/5983/medium_WNC_Nature_Center_1500399031-Screen_Shot_2017-07-18_at_1.23.49_PM.png'],
                       'Austin': ['https://cdn.vox-cdn.com/thumbor/c4ZKzDrJEnsYTJJmu-Jz65QNsG4=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/16389492/Mount_Bonnell_shutterstock.jpg',
                            'https://i.pinimg.com/originals/67/ef/52/67ef52b62a97ab3d9ab4aaea6e1a7734.jpg',
                            'https://images.unsplash.com/flagged/photo-1568917052807-c674bd9009b0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1400&q=80'],
                       'Boston': ['https://images.unsplash.com/flagged/photo-1568917052807-c674bd9009b0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1400&q=80',
                            'https://afar-production.imgix.net/uploads/images/post_images/images/H6SME2iDPZ/original_4bd330970c032d9223ecb01a28dd2170.jpg?1531776707?ixlib=rails-0.3.0&w=600&h=600&fit=crop&auto=format%2Ccompress&q=80',
                            'https://www.history.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTU3ODc4NjAyOTgwNzk2MTI3/hith-fenway-park-2.jpg'],
                       'Broward County': ['https://i.pinimg.com/originals/9b/a7/db/9ba7db18c0514b1c5b8b693cf2686a67.jpg',
                            'https://media-cdn.tripadvisor.com/media/photo-s/12/2b/f0/0b/photo1jpg.jpg',
                            'https://media-cdn.tripadvisor.com/media/photo-s/12/78/0b/3e/butterfly-world.jpg'],
                       'Cambridge': ['https://anhistorianabouttown.com/wp-content/uploads/2019/03/Kings-College-Gate-interior-short-1024x1024.jpeg',
                            'https://assets.atlasobscura.com/media/W1siZiIsInVwbG9hZHMvcGxhY2VfaW1hZ2VzLzMxZDVlNTJmLTM5YjItNDM5Yy1hOWMzLTAxNjUzNWVmYzM3MTgyYTk5MDJkMzg0MjNmMjVmZV9RdWVlbnMnX0NvbGxlZ2VfLV9NYXRoZW1hdGljYWxfQnJpZGdlLmpwZyJdLFsicCIsInRodW1iIiwiNTgweDU4MCMiXSxbInAiLCJjb252ZXJ0IiwiLXF1YWxpdHkgODEgLWF1dG8tb3JpZW50Il1d/Queens%27_College_-_Mathematical_Bridge.jpg',
                            'https://statues.vanderkrogt.net/Foto/gb/gbee073.jpg'],
                       'Chicago': ['https://liveatone.com/wp-content/uploads/2019/07/ONE_LUXE_APARTMENTS_WHEELING_ART_INSTITUTE_CHICAGO.jpg',
                            'https://loopchicago.com/assets/Uploads/8bf36eae8a/blog_happy-12th-birthday-millennium-park-v2__FillWzEyMDAsMTIwMF0.jpg',
                            'https://d1marr3m5x4iac.cloudfront.net/images/edpborder500/I0-001/039/261/783-2.jpeg_/navy-pier-83.jpeg'],
                       'Clark County': ['https://www.tripsavvy.com/thmb/et-H_WI35W4Z1YqZPaq_yvS4PtA=/3377x3377/smart/filters:no_upscale()/Fountains-Bellagio-Las-Vegas-1-3af96de921564e0b8ea2dd1f233cdf7b.jpg',
                            'https://www.waldorfastorialasvegas.com/wp-content/uploads/2019/07/las-vegas-strip-840x840.jpg',
                            'https://cdn.britannica.com/58/156458-050-68649A2F/Hoover-Dam-border-Colorado-River-Arizona-Nevada.jpg'],
                       'Columbus': ['https://media-cdn.tripadvisor.com/media/photo-s/0e/ea/eb/de/columbus-zoo.jpg',
                            'https://www.fpconservatory.org/wp-content/uploads/2017/07/KJJ_9057-600x600.jpg',
                            'https://psmag.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTUzMjEzMTA5NjU2MzY0NjY0/gettyimages-605876756.jpg'],
                       'Denver': ['https://img.grouponcdn.com/pwa_test/2RDoZnrXgxnsvkxqXVGcyhcFkXys/2R-669x446/v1/sc600x600.jpg',
                            'https://cdn.vox-cdn.com/thumbor/GwvqT9o8NnKEnaWL_69epdiBtT8=/0x0:2048x1536/1400x1400/filters:focal(828x420:1154x746):format(jpeg)/cdn.vox-cdn.com/uploads/chorus_image/image/52365515/8533619567_93262b4b95_k.0.jpeg',
                            'https://d.newsweek.com/en/full/1594773/colorado-state-capitol-building.jpg?w=1600&h=1600&q=88&f=15f7c8f1366fbf6d96759f99a83763f2'],
                       'Jersey City': ['https://i.guim.co.uk/img/media/f222c156d2f2d0ee68327f0233e9ed631c9519ca/0_0_3645_2186/master/3645.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=efe0f2456091d7fd2f8d8c6044d116e2',
                            'https://www.langan.com/wp-content/uploads/2017/02/Liberty-Science-Center-600.jpg',
                            'https://img.travelawaits.com/quill/4/8/9/0/a/1/4890a13ad8e016a14be7d6676629093276517572.jpg'],
                       'Los Angeles': ['https://i.pinimg.com/originals/0b/1b/d2/0b1bd22875454b01bcc87bc40d7072f0.jpg',
                            'https://media.cntraveler.com/photos/5ee255bf0196b768320d94f4/1:1/w_2848,h_2848,c_limit/DisneylandCalifornia-D6DEXF.jpg',
                            'https://tmd.discoverlosangeles.com/sites/default/files/media/activities/points_of_interest/griffith-observatory-hollywood-sign-sunset.jpg'],
                       'Nashville': ['https://assets.podomatic.net/ts/f0/cf/3e/allensircy/3000x3000_14380129.jpg',
                            'https://images.theconversation.com/files/248943/original/file-20181205-186055-spp99r.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=1200&h=1200.0&fit=crop',
                            'https://www.fifthandb.com/wp-content/uploads/2020/02/5B-home-740x740-1.jpg'],
                       'New Orleans': ['https://www.tripsavvy.com/thmb/_NtaX6kk61zl81DwiS2WHCw21AI=/2995x2995/smart/filters:no_upscale()/FrenchQuarter6-2607e9a35fb8479582c74e8e24893227.jpg',
                            'https://assets.simpleviewinc.com/simpleview/image/upload/c_fill,h_560,q_60,w_560/v1/clients/neworleans/NOTMC_33329_a48a1ee8-9e44-4bda-9824-d54fdb8097f1.jpg',
                            'https://bloximages.newyork1.vip.townnews.com/nola.com/content/tncms/assets/v3/editorial/a/20/a205af8a-d155-5c70-a6e0-18f69a3884dd/5dd72fa870112.image.jpg?crop=741%2C741%2C124%2C0&resize=1200%2C1200&order=crop%2Cresize'],
                       'New York City': ['https://cdn.vox-cdn.com/thumbor/JMqrPS2RmaDK6S5zaMuIw03I5Ns=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/18971698/151006_19_00_22_5DSR9489.jpg',
                            'https://www.history.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTY1MTc1MTk3ODI0MDAxNjA5/topic-statue-of-liberty-gettyimages-960610006-promo.jpg',
                            'https://www.thechatwalny.com/wp-content/uploads/sites/17/2018/03/Chatwal-New-York-Local-Attractions-Central-Park-Aerial-View-1024x1024.jpg'],
                       'Oakland': ['https://i.pinimg.com/originals/25/68/43/256843d4c25c33293ebcb2338c015f23.jpg',
                            'https://cdn.vox-cdn.com/thumbor/-6QwzuG16TmoHAd0m1-YOiarrSo=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/19253007/5717773834_213aff2481_k.jpg',
                            'https://cdn.vox-cdn.com/thumbor/jqYlPggQ5lX3bmrSd81ZSqkavxI=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/19239289/12th_Street_Entrance.jpg'],
                       'Pacific Grove': ['https://i.pinimg.com/originals/3a/c7/11/3ac7119ae3af18189b7c7a1bc02941cd.jpg',
                            'https://afar-production.imgix.net/uploads/images/post_images/images/7Casjl9ZqP/original_POI-0032_Point_Pinos_Lighthouse_Lisa_Corson-3789.jpg?1526438695?ixlib=rails-0.3.0&w=600&h=600&fit=crop&auto=format%2Ccompress&q=80',
                            'https://d3qvqlc701gzhm.cloudfront.net/thumbs/baa64daf27e9c7ed96f230c85217f0d4bc5010dc99c147bf9c425e511b907d15-375.jpg'],
                       'Portland': ['https://3hm4vx15otpx2n5mp13bqbsk-wpengine.netdna-ssl.com/wp-content/uploads/2012/07/washington-playground-alameda.jpg',
                            'https://bloximages.newyork1.vip.townnews.com/yakimaherald.com/content/tncms/assets/v3/editorial/3/65/3650d6f6-d365-514c-944d-11fc08c00069/5da602b812ee6.image.jpg?crop=1237%2C1237%2C219%2C0&resize=1237%2C1237&order=crop%2Cresize',
                            'https://assets.atlasobscura.com/media/W1siZiIsInVwbG9hZHMvcGxhY2VfaW1hZ2VzL2U4MmFiOWVkNTI4NDA3MWQ4M18xMjAwcHgtUm9zZV9HYXJkZW4sX0p1bmVfMjAxNi5qcGciXSxbInAiLCJ0aHVtYiIsIjU4MHg1ODAjIl0sWyJwIiwiY29udmVydCIsIi1xdWFsaXR5IDgxIC1hdXRvLW9yaWVudCJdXQ/1200px-Rose_Garden%2C_June_2016.jpg'],
                       'Rhode Island': ['https://townsquare.media/site/518/files/2018/01/WaterFire-Providence.jpg',
                            'https://www.tripsavvy.com/thmb/9fFcgrH471aBDFhAieCofj8TIns=/2832x2832/smart/filters:no_upscale()/Newport-Cliff-Walk-5a86598e8e1b6e0036a87594.jpg',
                            'https://i.pinimg.com/originals/7b/47/25/7b4725810687e89ff460fc94ea2f9ba9.jpg'],
                       'Salem': ['https://media.architecturaldigest.com/photos/5d1a2c7c8b62fb0009f89f9e/1:1/w_3011,h_3011,c_limit/PeabodyEssexMuseum%20photo%20by%20Aislinn%20Weidele_Ennead%20Architects_1.jpg',
                            'https://www.tripsavvy.com/thmb/e8xRVNJIFu0jOKAqeO0gJ6TCuuI=/1000x1000/smart/filters:no_upscale()/salemwitchmuseum-78e395a5a04b4ead89da4f215c9c7406.jpg',
                            'https://i.pinimg.com/originals/70/4e/d1/704ed19e7170ca660d8709f89603bfe7.png'],
                       'San Clara County': ['https://cdn.vox-cdn.com/thumbor/KlBHBhqZYo02fsvmGpdsWu282Q4=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/21923127/1175987442.jpg.jpg',
                            'https://media-cdn.tripadvisor.com/media/photo-s/14/41/0e/61/photo1jpg.jpg',
                            'https://www.scu.edu/media/offices/global-engagement/photos-for-buttons/cat-1/cat-8/LANDSCAPES_Yue-Hu_Denver.jpg'],
                       'San Diego': ['https://i2.wp.com/www.hachettebookgroup.com/wp-content/uploads/2019/01/CA_SanDiego_BalboaPark_Dreamstime.jpg?resize=1080%2C1080&ssl=1',
                            'https://i.pinimg.com/originals/f8/d9/5d/f8d95d0b3099ad7838cdcdf263dc9c0c.jpg',
                            'https://geltechsolutions.com/fireice/wp-content/uploads/2018/07/San-Diego-Zoo-Challenge.jpg'],
                       'San Francisco': ['https://www.history.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTY1MTc3MjE0MzExMDgxNTQ1/topic-golden-gate-bridge-gettyimages-177770941.jpg',
                            'https://img-aws.ehowcdn.com/560x560p/s3-us-west-1.amazonaws.com/contentlab.studiod/getty/8ca37fc971794b4eafdafb65d38159d7',
                            'https://img.static-kl.com/images/media/4FF03D3A-CA85-456A-8A96A1CF42192208?aspect_ratio=1:1&min_width=912'],
                       'San Mateo County': ['https://i.pinimg.com/originals/c4/09/4b/c4094b7335f6444d356eb239a5d01ae7.jpg',
                            'https://i.pinimg.com/originals/9a/d2/29/9ad2292669c3196de082d9a0412388c1.jpg',
                            'https://i.guim.co.uk/img/media/50f7a1efd00676dba5d799e46ccd22689112fad1/0_339_5056_3035/master/5056.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=1ff9a74fe6a877d22805b2a8c8e08edf'],
                       'Santa Cruz County': ['https://www.sanjose.org/sites/default/files/styles/listing_detail_image/public/2017-10/r_1.jpg?itok=rsqX2kzU',
                            'https://www.sanjose.org/sites/default/files/styles/listing_detail_image/public/2017-10/p_2.jpg?itok=a_uAa1_4',
                            'https://www.sanjose.org/sites/default/files/styles/listing_detail_image/public/2017-10/wsii-2102_0.jpg?itok=WYRN28qO'],
                       'Seattle': ['https://www.panpacificseattle.com/wp-content/uploads/2017/08/Chihuly-Garden-Glass-in-Seattle.jpg',
                            'https://cdn.vox-cdn.com/thumbor/ODal3bbEgzSe6w2LyJ0jWcMks70=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/10915759/PikePlaceMarket1.jpg',
                            'https://www.tripsavvy.com/thmb/9F-23TwLMR2vOC5OQkye71Xuuws=/1369x1369/smart/filters:no_upscale()/GettyImages-610712690-5c3ba9c646e0fb00018dead8.jpg'],
                       'Twin Cities MSA': ['https://i.pinimg.com/736x/5a/7e/db/5a7edbfa4d398ddc5a73299df429058d.jpg',
                            'https://www.americanrivers.org/wp-content/uploads/2016/03/B-9-713x713.png',
                            'https://d1marr3m5x4iac.cloudfront.net/images/edpborder500/I0-001/004/400/621-0.jpeg_/walker-art-center-21.jpeg'],
                       'Washington D.C.': ['https://washington-org.s3.amazonaws.com/s3fs-public/styles/gallery_full/public/trippingovertravel_winter-evening-columns-at-wwii-memorial_yesmydccool.jpg?itok=Q1ACVt5-',
                            'https://pbs.twimg.com/profile_images/1016670443560988672/bLMYqlx9.jpg',
                            'https://media.architecturaldigest.com/photos/56c7af26cd3bcb326e99b545/1:1/w_3075,h_3075,c_limit/lincoln-center-renovation-01.jpg']}


nearby_city_name_dict = { 'Asheville': ['Nature Center (WNC)', 'Biltmore Estate', 'Blue Ridge Parkway'],
                          'Austin': ['Lake Austin', 'Zilker Park', 'Texas Capitol'],
                          'Boston': ['Faneulli Hall', 'Freedom Trail', 'Fenway Park'],
                          'Broward County': ['Las Olas Boulevard', 'Flamingo Park', 'Butterfly Park'],
                          'Cambridge': ['Kings College',
                          'Mathematical Bridge',
                          "Great St. Mary's Church"],
                          'Chicago': ['Art Institute', 'Millenium Park', 'Navy Pier'],
                          'Clark County': ['Bellagio Hotel and Casino',
                          'Las Vegas Strip',
                          'Hoover Dam'],
                          'Columbus': ['Columbus Zoo and Aquarium',
                          'Franklin Park Conservatory',
                          'Centre of Science and Industry'],
                          'Denver': ['Botanic Gardens', 'Art Museum', 'Denver State Capitol'],
                          'Jersey City': ['Atlantic City', 'Liberty Science Center', 'Asbury Park'],
                          'Los Angeles': ['Universal Studios', 'Disney Land', 'Griffith Observatory'],
                          'Nashville': ['Ryman Auditorium', 'The Parthenon', 'The Broadway'],
                          'New Orleans': ['French Quarter',
                          'Mardi Gras',
                          'National World War II Museum'],
                          'New York City': ['Empire State Building',
                          'Statue of Liberty',
                          'Central Park'],
                          'Oakland': ['Lake Merritt',
                          'Jack London Square',
                          'Oakland Museum of California'],
                          'Pacific Grove': ['Monterey Bay Aquarium', 'Pinos Lighthouse', 'Cannery Row'],
                          'Portland': ['Washington Park', 'Pittock Mansion', 'Rose Test Garden'],
                          'Rhode Island': ['Water Fire Providence',
                          'Cliff Walk Newport',
                          'The Breakers Newport'],
                          'Salem': ['Peabody Essex Museum', 'Witch Museum', 'Maritime Historic Museum'],
                          'San Clara County': ['Levis Stadium',
                          'Intel Corp. and Museum',
                          'Santa Clara University'],
                          'San Diego': ['Balboa Park', 'Harbour Cruise', 'San Diego Zoo'],
                          'San Francisco': ['Golden Gate Bridge',
                          'Alcatraz Island',
                          'Golden Gate Park'],
                          'San Mateo County': ['Nuevo State Park',
                          'Mavericks Beach',
                          'Pigeon Point Lighthouse'],
                          'Santa Cruz County': ['Henry Cowell Redwoods State Park',
                          'Natural Bridges State Beach',
                          'Roaring Camp'],
                          'Seattle': ['Chihuly Garden and Glass', 'Pike Place Market', 'Space Needle'],
                          'Twin Cities MSA': ['Cathedral of St. Paul',
                          'Mississippi National River',
                          'Walker Art Center'],
                          'Washington D.C.': ['World War II Memorial',
                          'National Air and Space Museum',
                          'Lincoln Memorial']}


nearby_id_name_dict = {0: ['Nature Center (WNC)', 'Biltmore Estate', 'Blue Ridge Parkway'],
                        1: ['Lake Austin', 'Zilker Park', 'Texas Capitol'],
                        2: ['Faneulli Hall', 'Freedom Trail', 'Fenway Park'],
                        3: ['Las Olas Boulevard', 'Flamingo Park', 'Butterfly Park'],
                        4: ['Kings College', 'Mathematical Bridge', "Great St. Mary's Church"],
                        5: ['Art Institute', 'Millenium Park', 'Navy Pier'],
                        6: ['Bellagio Hotel and Casino', 'Las Vegas Strip', 'Hoover Dam'],
                        7: ['Columbus Zoo and Aquarium', 'Franklin Park Conservatory','Centre of Science and Industry'],
                        8: ['Botanic Gardens', 'Art Museum', 'Denver State Capitol'],
                        9: ['Atlantic City', 'Liberty Science Center', 'Asbury Park'],
                        10: ['Universal Studios', 'Disney Land', 'Griffith Observatory'],
                        11: ['Ryman Auditorium', 'The Parthenon', 'The Broadway'],
                        12: ['French Quarter', 'Mardi Gras', 'National World War II Museum'],
                        13: ['Empire State Building', 'Statue of Liberty', 'Central Park'],
                        14: ['Lake Merritt', 'Jack London Square', 'Oakland Museum of California'],
                        15: ['Monterey Bay Aquarium', 'Pinos Lighthouse', 'Cannery Row'],
                        16: ['Washington Park', 'Pittock Mansion', 'Rose Test Garden'],
                        17: ['Water Fire Providence', 'Cliff Walk Newport', 'The Breakers Newport'],
                        18: ['Peabody Essex Museum', 'Witch Museum', 'Maritime Historic Museum'],
                        19: ['Balboa Park', 'Harbour Cruise', 'San Diego Zoo'],
                        20: ['Golden Gate Bridge', 'Alcatraz Island', 'Golden Gate Park'],
                        21: ['Nuevo State Park', 'Mavericks Beach', 'Pigeon Point Lighthouse'],
                        22: ['Levis Stadium', 'Intel Corp. and Museum', 'Santa Clara University'],
                        23: ['Henry Cowell Redwoods State Park','Natural Bridges State Beach','Roaring Camp'],
                        24: ['Chihuly Garden and Glass', 'Pike Place Market', 'Space Needle'],
                        25: ['Cathedral of St. Paul','Mississippi National River','Walker Art Center'],
                        26: ['World War II Memorial','National Air and Space Museum','Lincoln Memorial']}