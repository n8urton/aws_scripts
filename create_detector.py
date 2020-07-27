#!/usr/bin/env python3

import boto3


def create_detector(client):
    client.create_detector(Enable=True)


def get_regions():
    client = boto3.client('ec2')
    return [region['RegionName'] for region in client.describe_regions()['Regions']]


def create_gd_client(region_name):
# Create GuardDuty client
    return boto3.client(service_name = 'guardduty', region_name=region_name)


def get_detector_status(region_name):
#Get the GuardDuty Detector for the current AWS Region
    gd = create_gd_client(region_name)

    detector=gd.list_detectors()
    #print(detector)
    if len(detector['DetectorIds']) > 0:
        detector_id = detector['DetectorIds'][0]
        print('GuardDuty Detector exists in Region ' + region_name + ' Detector Id: ' + detector_id)
    else:
        print('GuardDuty Detector does not exist in Region ' + region_name)
        # Uncomment to create detector in region
        #print('Creating Detector in ' + region_name + ' ...')
        #create_detector(gd)


def main():
    regions = get_regions()
    for region in regions:
        get_detector_status(region)


if __name__== '__main__':
    main()
#print(get_regions())

