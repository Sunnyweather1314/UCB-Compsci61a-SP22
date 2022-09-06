(define (cadr lst) (car (cdr lst)))

(define (make-kwlist1 keys values)
    (list keys values)
  )

(define (get-keys-kwlist1 kwlist) (car kwlist))

(define (get-values-kwlist1 kwlist)
   (cadr kwlist))

(define (make-kwlist2 keys values)
    (if (or (null? keys) (null? values))
        nil
        (cons (list (car keys) (car values)) (make-kwlist2 (cdr keys) (cdr values)))))

(define (get-keys-kwlist2 kwlist) (map (lambda(a) (car a)) kwlist))

(define (get-values-kwlist2 kwlist)
  (map (lambda(a) (cadr a)) kwlist))

(define (add-to-kwlist kwlist key value)
  (make-kwlist (append (get-keys-kwlist kwlist) (list key))
        (append (get-values-kwlist kwlist) (list value))))

(define (get-first-from-kwlist kwlist key)
  (define (inner kwlist_key kwlist_value)
      (cond ((null? kwlist_key) nil)
      ((equal? (car kwlist_key) key) (car kwlist_value))
      (else (inner (cdr kwlist_key) (cdr kwlist_value)))))
  (inner (get-keys-kwlist kwlist) (get-values-kwlist kwlist))
  )

(define (prune-expr expr)
  (define (prune-helper lst) 
          (cond ((null? lst) nil)
                ((null? (cdr lst)) (cons (car lst) nil))
              (else (cons (car lst) (prune-helper (cdr (cdr lst)))))))
    (append (cons (car expr) nil) (prune-helper (cdr expr)))
)

(define (curry-cook formals body) 
(if (null? formals) body `(lambda(,(car formals)) ,(curry-cook (cdr formals) body)))
    )

(define (curry-consume curries args)
(if (null? args) curries (curry-consume (curries (car args)) (cdr args)))  )
