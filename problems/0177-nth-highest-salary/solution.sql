CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N=N-1;
  RETURN (
      # Write your MySQL query statement below.
       SELECT DISTINCT salary as getNthHighestSalary from Employee ORDER BY Salary Desc LIMIT 1 OFFSET N );
END
