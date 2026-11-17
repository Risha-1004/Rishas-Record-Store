CREATE DATABASE IF NOT EXISTS recordstore;
USE recordstore;

CREATE TABLE Vinyls (
    ItemID INT PRIMARY KEY,
    Title VARCHAR(50),
    Artist VARCHAR(100),
    Genre VARCHAR(30),
    Price INT,
    CopiesSold INT
);

INSERT INTO Vinyls VALUES 
(101, 'Thriller', 'Michael Jackson', 'Pop', 2100, 450),
(110, 'Charm', 'Clairo', 'Indie & Folk', 2800, 490),
(105, 'Melodrama', 'Lorde', 'Pop', 2400, 310),
(114, 'You Seem Pretty Sad For A Girl So In Love', 'Olivia Rodrigo', 'Pop', 2200, 380),
(112, 'Brat', 'Charli XCX', 'Electronic & Dance', 2600, 410),
(102, 'Ego Death At A Bachelorette Party', 'Hayley Williams', 'Alternative Rock', 2500, 150),
(106, 'Fetch the Bolt Cutters', 'Fiona Apple', 'Alternative Rock', 2700, 120),
(104, 'Punisher', 'Phoebe Bridgers', 'Indie & Folk', 2300, 280),
(107, 'Back to Black', 'Amy Winehouse', 'R&B & Soul', 1850, 340),
(109, 'Lemonade', 'Beyonce', 'R&B & Soul', 3200, 290),
(111, 'The Miseducation of', 'Lauryn Hill', 'R&B & Soul', 1900, 400),
(113, 'Blonde', 'Frank Ocean', 'R&B & Soul', 3500, 360),
(108, 'Aaliyah', 'Aaliyah', 'R&B & Soul', 1700, 210),
(103, 'To Pimp A Butterfly', 'Kendrick Lamar', 'Hip-Hop', 2900, 420),
(115, 'Folklore', 'Taylor Swift', 'Indie & Folk', 2800, 465);

SELECT * FROM Vinyls;
