CREATE TABLE country (
  PRIMARY KEY (id)
  , id    SMALLSERIAL
  , name  TEXT          NOT NULL
)

CREATE TABLE user (
  PRIMARY KEY (id)
  , id                UUID          UNIQUE
  , creation_time     TIMESTAMPTZ   NOT NULL
)

CREATE TABLE league (
  PRIMARY KEY (id)
  , id                UUID
  , name              TEXT          UNIQUE
                                    NOT NULL
  , creation_time     TIMESTAMPTZ   NOT NULL
  , current_date      DATE          NOT NULL
  , private           BOOLEAN       NOT NULL
  , private_password
);

CREATE TABLE team (
  PRIMARY KEY (id)
  , id                UUID
  , name              TEXT          NOT NULL
  , owner_id          UUID          REFERENCES user(id)
);

CREATE TABLE player_status (
  PRIMARY KEY (id)
  , id    SMALLSERIAL
  , name  TEXT
)

CREATE TABLE player_contract (
  PRIMARY KEY (id)
  , id
  , start_date        DATE          NOT NULL
  , length            SMALLINT      NOT NULL
  ,
)

CREATE TABLE player (
  PRIMARY KEY (id)
  , id                UUID
  , name              TEXT          NOT NULL
  , birthdate         DATE          NOT NULL
  , nicknames         TEXT[]        NOT NULL
  , league_id         UUID          NOT NULL
                                    REFERENCES league(id)
  , team_id           UUID          REFERENCES team(id)
  , contract_id       UUID          REFERENCES player_contract(id)
  , status_id         SMALLSERIAL   REFERENCES player_status(id)
)

CREATE TABLE free_agent (
  , id                UUID
  , league_id         UUID
  , player_id         UUID
)