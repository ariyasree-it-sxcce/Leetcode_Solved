/* 
IF(condition, value_if_true, value_if_false)

Acts like if–else

Evaluated row by row 
*/

UPDATE Salary 
SET sex = IF (sex='m','f','m')

-- IF ( sex='m' ,  'f' ,   'm' )
--     condition   true    false
-- if m (true) then f else: m (false) then m