(define (split-at lst n)
  (cond 
    ((null? lst)
     (cons nil nil))
    ((= n 0)
     (cons nil lst))
    (else
     (let ((result (split-at (cdr lst) (- n 1))))
       (cons (cons (car lst) (car result)) (cdr result))))))

; Tree Abstraction
; Constructs tree given label and list of branches
(define (tree label branches)
  (cons label branches))

; Returns the label of the tree
(define (label t) (car t))

; Returns the list of branches of the given tree
(define (branches t) (cdr t))

; Returns #t if t is a leaf, #f otherwise
(define (is-leaf t) (null? (branches t)))

(define (filter-odd t)
  (cond 
    ((even? (label t))
     (tree nil (map filter-odd (branches t))))
    ((is-leaf t)
     t)
    (else
     (tree (label t) (map filter-odd (branches t))))))

(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))

(define (swap expr)
  (define (inner expr)
    (let ((v1 (eval (car expr)))
          (v2 (eval (cadr expr))))
      (cond 
        ((< v1 v2)
         (append (list (cadr expr) (car expr)) (cddr expr)))
        (else
         expr))))
  (cons (car expr) (inner (cdr expr)))
  )


