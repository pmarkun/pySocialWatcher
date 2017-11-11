# -*- coding: utf-8 -*-
import time
SAVE_EMPTY = True
SLEEP_TIME = 8
SAVE_EVERY = 300
MAX_NUMBER_TRY = 10
INITIAL_TRY_SLEEP_TIME = 300
API_UNKOWN_ERROR_CODE_1 = 1
API_UNKOWN_ERROR_CODE_2 = 2
INVALID_PARAMETER_ERROR = 100
FEW_USERS_IN_CUSTOM_LOCATIONS_SUBCODE_ERROR = 1885036
NUMBER_OF_REQUESTS_PER_BUCKET = 100
UNIQUE_TIME_ID = str(time.time()).split(".")[0]
DATAFRAME_SKELETON_FILE_NAME = "dataframe_skeleton_" + UNIQUE_TIME_ID + ".csv"
DATAFRAME_TEMPORARY_COLLECTION_FILE_NAME = "dataframe_collecting_" + UNIQUE_TIME_ID + ".csv"
DATAFRAME_AFTER_COLLECTION_FILE_NAME = "dataframe_collected_finished_" + UNIQUE_TIME_ID + ".csv"
DATAFRAME_AFTER_COLLECTION_FILE_NAME_WITHOUT_FULL_RESPONSE = "collect_finished_clean" + UNIQUE_TIME_ID + ".csv"
DEFAULT_DUMB_TARGETING = {'geo_locations': {u'regions': [{u'key': u'3843'}], 'location_types': ['home']}, 'genders': [0], }
REACHESTIMATE_URL = "https://graph.facebook.com/v2.10/act_{}/reachestimate"
GRAPH_SEARCH_URL = "https://graph.facebook.com/v2.10/search"
TARGETING_SEARCH_URL = "https://graph.facebook.com/v2.10/act_{}/targetingsearch"
TOKENS = []
INPUT_AGE_RANGE_FIELD = "ages_ranges"
INPUT_GEOLOCATION_FIELD = "geo_locations"
INPUT_LIFEEVENTS_FIELD = "life_events"
INPUT_GEOLOCATION_LOCATION_TYPE_FIELD = "location_types"
DEFAULT_GEOLOCATION_LOCATION_TYPE_FIELD = ["home"]
INPUT_GENDER_FIELD = "genders"
INPUT_INTEREST_FIELD = "interests"
INPUT_CONNECTIONS_FIELD = "connections"
GROUP_ID_FIELD = "group_id"
INPUT_BEHAVIOR_FIELD = "behavior"
INPUT_SCHOLARITY_FIELD = "scholarities"
INPUT_LANGUAGE_FIELD = "languages"
INPUT_FAMILYSTATUS_FIELD = "family_statuses"
INPUT_RELATIONSHIPSTATUS_FIELD = "relationship_statuses"
TARGETING_FIELD = "targeting"
RESPONSE_FIELD = "response"
AUDIENCE_FIELD = "audience"
ALLFIELDS_FIELD = "all_fields"
INPUT_NAME_FIELD = "name"
PERFORM_AND_BETWEEN_GROUPS_INPUT_FIELD = "perform_AND_between_groups"
MIN_AGE = "min"
MAX_AGE = "max"
DETAILS_FIELD_FROM_FACEBOOK_TARGETING_SEARCH = ["id", "name", "type", "description", "audience_size", "path","key","supports_city","supports_region"]
API_INTEREST_FIELD = "interests"
API_CONNECTIONS_FIELD = "connections"
API_BEHAVIOR_FIELD = "behaviors"
API_HOUSEHOLD_COMPOSITION_FIELD = "household_composition"
API_LIFEEVENTS_FIELD = "life_events"

INPUT_HOUSEHOLD_COMPOSITION_FIELD = "household_composition"
INPUT_CITIZENSHIP_BEHAVIOR_SUBFIELD = "citizenship"
INPUT_ACCESS_DEVICES_BEHAVIOR_SUBFIELD = "access_device"
API_SCHOLARITY_FIELD = "education_statuses"
API_FAMILYSTATUS_FIELD = "family_statuses"
API_RELATIONSHIPSTATUS_FIELD = "relationship_statuses"
API_LANGUAGES_FIELD = "locales"
API_GENDER_FIELD = "genders"
API_MIN_AGE_FIELD = "age_min"
API_MAX_AGE_FIELD = "age_max"
API_GEOLOCATION_FIELD = "geo_locations"
API_PUBLISHER_PLATFORMS_FIELD = "publisher_platforms"
PUBLISHER_PLATFORM_DEFAULT = ["facebook"]

INPUT_FIELDS_TO_COMBINE = [
    INPUT_INTEREST_FIELD,
    INPUT_CONNECTIONS_FIELD,
    INPUT_AGE_RANGE_FIELD,
    INPUT_GENDER_FIELD,
    INPUT_BEHAVIOR_FIELD,
    INPUT_SCHOLARITY_FIELD,
    INPUT_LANGUAGE_FIELD,
    INPUT_FAMILYSTATUS_FIELD,
    INPUT_RELATIONSHIPSTATUS_FIELD,
    INPUT_LIFEEVENTS_FIELD,
    INPUT_GEOLOCATION_FIELD,
    INPUT_HOUSEHOLD_COMPOSITION_FIELD
]

DATAFRAME_COLUMNS = [INPUT_NAME_FIELD] + INPUT_FIELDS_TO_COMBINE + [ALLFIELDS_FIELD, TARGETING_FIELD, RESPONSE_FIELD, AUDIENCE_FIELD ]

ALLOWED_FIELDS_IN_INPUT = DATAFRAME_COLUMNS + [PERFORM_AND_BETWEEN_GROUPS_INPUT_FIELD] + [API_PUBLISHER_PLATFORMS_FIELD]

ADVANCE_TARGETING_FIELDS_TYPE_ARRAY_IDS = [
    INPUT_INTEREST_FIELD,
    INPUT_CONNECTIONS_FIELD,
    INPUT_BEHAVIOR_FIELD,
    INPUT_CITIZENSHIP_BEHAVIOR_SUBFIELD,
    INPUT_ACCESS_DEVICES_BEHAVIOR_SUBFIELD,
    INPUT_LIFEEVENTS_FIELD,
    INPUT_FAMILYSTATUS_FIELD,
    INPUT_HOUSEHOLD_COMPOSITION_FIELD
]

ADVANCE_TARGETING_FIELDS_TYPE_ARRAY_INTEGER = [
    INPUT_SCHOLARITY_FIELD, INPUT_RELATIONSHIPSTATUS_FIELD
]
INPUT_TO_API_FIELD_NAME = {
    INPUT_GENDER_FIELD : API_GENDER_FIELD,
    INPUT_INTEREST_FIELD: API_INTEREST_FIELD,
    INPUT_CONNECTIONS_FIELD: API_CONNECTIONS_FIELD,
    INPUT_BEHAVIOR_FIELD: API_BEHAVIOR_FIELD,
    INPUT_CITIZENSHIP_BEHAVIOR_SUBFIELD: API_BEHAVIOR_FIELD,
    INPUT_HOUSEHOLD_COMPOSITION_FIELD: API_HOUSEHOLD_COMPOSITION_FIELD,
    INPUT_ACCESS_DEVICES_BEHAVIOR_SUBFIELD: API_BEHAVIOR_FIELD,
    INPUT_LIFEEVENTS_FIELD: API_LIFEEVENTS_FIELD,
    INPUT_SCHOLARITY_FIELD: API_SCHOLARITY_FIELD,
    INPUT_FAMILYSTATUS_FIELD: API_FAMILYSTATUS_FIELD,
    INPUT_RELATIONSHIPSTATUS_FIELD: API_RELATIONSHIPSTATUS_FIELD
}

ADVANCE_TARGETING_FIELDS = [
    INPUT_INTEREST_FIELD, INPUT_CONNECTIONS_FIELD, INPUT_BEHAVIOR_FIELD, INPUT_SCHOLARITY_FIELD, INPUT_FAMILYSTATUS_FIELD, INPUT_BEHAVIOR_FIELD
]

FAKE_DATA_RESPONSE_CONTENT = '{"mockResponse":true, "data": { "users":0, 	"bid_estimations":[ { "unsupported":false, "location":0, "reach_min":0,	"reach_max":0, "cpm_curve_data":"",	"cpc_curve_data":"", "cpa_curve_data":"", "dedup_winning_rate":0,"dedup_status":0, "pacing_status":0,"account_budget":0,"estimate_DAU":0, "curve":[	{"bid":0,"spend":0,"reach":0,"impressions":0,"actions":0}],"trace_id":"0","bid_amount_min":0,"bid_amount_median":0,"bid_amount_max":0}],"estimate_ready":false}}'