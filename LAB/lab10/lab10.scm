(define (over-or-under num1 num2)
   (if (> num1 num2)
       1
       (if (= num1 num2)
           0
           -1
        )
    )
)
       
      

(define (over-or-under num1 num2)
    (cond 
        ((> num1 num2) 1)
        ((= num1 num2) 0)
        ((< num1 num2) -1)
    )
)

(define (make-adder num) (lambda (y) (+ y num)))

(define (composed f g) (lambda (x) (f (g x))))

(define (square n) (* n n))

(define (pow base exp) 
    (if (= exp 1)
        base
        (if (even? exp)
            (square (pow base (/ exp 2)))
            (* base (pow base (- exp 1)))
        )
    )
)

(if (not (print 1))
    (print 2)
    (print 3))
