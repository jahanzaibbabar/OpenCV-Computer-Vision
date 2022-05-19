# # from pydrive.auth import GoogleAuth
# # from pydrive.drive import GoogleDrive
# #
# # # Login to Google Drive and create drive object
# # g_login = GoogleAuth()
# # g_login.LocalWebserverAuth()
# # drive = GoogleDrive(g_login)
# # # Importing os and glob to find all PDFs inside subfolder
# # import os
# #
# file = "img2.jpg"
# #
# # with open(file, "rb") as f:
# #     fn = os.path.basename(f.name)
# #     file_drive = drive.CreateFile({'title': fn , 'mimeType': 'image/jpeg'})
# #
# #     file_drive.SetContentString(file)
# #     file_drive.Upload()
#
# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive
#
# gauth = GoogleAuth()
# gauth.LocalWebserverAuth()
# drive = GoogleDrive(gauth)
#
# f = drive.CreateFile({'title': file, 'mimeType': 'image/jpeg'})
# f.SetContentFile(file)
# f.Upload()
# print ("The file: " + file + " has been uploaded")


# import cv2
#
# cap = cv2.VideoCapture(1)
# while True:
#     success, img = cap.read()
#
#     cv2.imshow("img", img)
#
#     if cv2.waitKey(1) & 0xff == ord('q'):
#         break

l1 = [1,2,3,4]
print(l1)
for x,y,a,s in l1:
     print(s)