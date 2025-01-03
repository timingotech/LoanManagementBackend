BEGIN;
--
-- Create model User
--
CREATE TABLE "accounts_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "avatar" varchar(100) NOT NULL, "balance" decimal NOT NULL, "loan_amount" decimal NOT NULL, "loan_status" varchar(20) NOT NULL, "num_transactions" integer NOT NULL);
--
-- Create model Transaction
--
CREATE TABLE "accounts_transaction" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "date" date NOT NULL, "amount" decimal NOT NULL, "description" text NOT NULL, "user_id" bigint NOT NULL REFERENCES "accounts_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "accounts_transaction_user_id_e9a98e81" ON "accounts_transaction" ("user_id");
COMMIT;
