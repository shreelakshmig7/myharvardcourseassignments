-- Keep a log of any SQL queries you execute as you solve the mystery.

--All you know is that the theft took place on July 28, 2023 and that it took place on Humphrey Street.
SELECT * FROM crime_scene_reports WHERE day = 28 AND month = 7 AND year = 2023 AND street = 'Humphrey Street';
-- | 295 | 2023 | 7     | 28  | Humphrey Street | Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
                                        --Interviews were conducted today with three witnesses who were present at the time
                                        --each of their interview transcripts mentions the bakery. |

-- As per the crime_scene_reports data, checking interviews table data for the information
SELECT * FROM interviews WHERE day = 28 AND month = 7 AND year = 2023;

--  As per the interviews table data - According to Ruth statement collecting the parking lot data
SELECT * FROM bakery_security_logs WHERE day = 28 AND month = 7 AND year = 2023 AND hour = 10 AND activity = 'exit';

-- As per the interviews table data - According to Eugene statement collecting the  ATM on Leggett Street data
SELECT * FROM atm_transactions WHERE day = 28 AND month = 7 AND year = 2023
AND atm_location = 'Leggett Street' and transaction_type = 'withdraw';

-- Getting info of the owner of the cars
SELECT * FROM people
WHERE license_plate IN ('5P2BI95', '94KL13X','6P58WS2','4328GD8','G412CB7','L93JTIZ','322W7JE','0NTHK55');

-- fetching info of people who were found both in bakery parking lot and atm_transactions location
SELECT * FROM people JOIN bank_accounts ON people.id = bank_accounts.person_id
WHERE people.license_plate IN ('5P2BI95', '94KL13X','6P58WS2','4328GD8','G412CB7','L93JTIZ','322W7JE','0NTHK55')
AND bank_accounts.account_number IN
('28500762', '28296815', '76054385', '49610011', '16153065', '25506511', '81061156', '26013199');


-- As per the interviews table data - According to Raymond statement collecting the phone_calls data
-- (which lasted less than a min) of those people who were shortlisted above
SELECT * FROM phone_calls WHERE day = 28 AND month = 7 AND year = 2023
AND caller IN ('(367) 555-5533', '(770) 555-1861', '(829) 555-5269', '(389) 555-5198 ') AND duration <= 60;


-- As per the interviews table data - According to Raymond statement 2nd part i.e.,
--theif planning to take the earliest flight of next day i.e., 29 july 2023

SELECT * FROM flights JOIN airports ON flights.origin_airport_id = airports.id
WHERE flights.day = 29 AND flights.month = 7 AND flights.year = 2023 AND airports.city = 'Fiftyville'
ORDER BY flights.hour, flights.minute;

-- As per the interviews table data - According to Raymond statement which has two main points
-- phone call and taking next day earliest flight.
-- Merging both the dataset i.e., 2 persons we got from phone call and the flights took by these people on 29 july 2023

SELECT people.name, people.phone_number, people.passport_number, passengers.flight_id FROM people
JOIN passengers ON people.passport_number = passengers.passport_number
WHERE passengers.flight_id IN (36, 43, 23) AND people.phone_number IN ('(367) 555-5533', '(770) 555-1861');

-- This will trace us to the theif - BRUCE


-- getting the city he escaped to
SELECT airports.city FROM airports JOIN flights ON airports.id = flights.destination_airport_id
WHERE flights.id = 36;
--- So the theif escaped to New York City


-- to find the accomplice if we go back to the shortlist phonecalls result set,
-- we had bruce phone number as caller and need to fetch receiver's details
SELECT people.name, people.phone_number FROM people
JOIN phone_calls ON people.phone_number = phone_calls.receiver
WHERE phone_calls.day = 28 AND phone_calls.month = 7 AND phone_calls.year = 2023 AND phone_calls.caller = '(367) 555-5533' AND phone_calls.duration <= 60;

-- So the accomplice is Robin
